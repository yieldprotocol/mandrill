import asyncio
import json
import os
import random
import re


async def generate(instructor, **kwargs):
    """Generator for generic/general training data."""
    config = instructor.instructors.get("general")
    if not config:
        return
    target_count = config.get("count")
    if target_count is None:
        target_count = instructor.default_count
    target_count = int(target_count)
    if not target_count:
        return

    # Load the prompt template.
    path = config.get("prompt_path", "general.txt")
    if not os.path.exists(path):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", path)
    with open(path) as infile:
        template = infile.read()

    # Load the topics.
    topics = instructor.get_instructor_topics(config)
    topic_index = random.randint(0, len(topics) - 1)

    # API params, overriding defaults with this instructor's config.
    api_params = {**instructor.api_params, **config.get("api_params", {})}

    # Min similarity score.
    min_score = config.get("min_docsearch_score")
    if min_score is None:
        min_score = instructor.min_docsearch_score
    min_score = float(min_score)

    # Generate the instruction/response pairs until we reach the target count.
    batch_size = config.get("batch_size")
    if batch_size is None:
        batch_size = instructor.default_batch_size
    batch_size = int(batch_size)
    if "general" not in instructor.instructor_counts:
        instructor.instructor_counts["general"] = 0
    language = config.get("language") or instructor.language
    flesch = config.get("flesch") or instructor.default_flesch
    while instructor.instructor_counts["general"] < target_count:
        # Inject the topics to use for this batch.
        current_topics = []
        for _ in range(batch_size):
            current_topics.append(topics[topic_index])
            topic_index += 1
            if topic_index >= len(topics):
                topic_index = 0
        topics_str = "\n".join(
            [
                f" * instruction {idx + 1} must be related to topic: {json.dumps(topic)}"
                for idx, topic in enumerate(current_topics)
            ]
        )

        # Get a batch of instructions.
        prompt = template.format(
            batch_size=batch_size,
            topics=topics_str,
            topic_avoidance=instructor.topic_avoidance,
            language=language,
            flesch=flesch,
        )
        response = await instructor.generate_response(prompt, **api_params)
        if not response:
            continue

        # Parse instructions and generate responses.
        futures = []
        instructions = []
        for instruction in re.findall(
            r"(?:^|\n)TSK \d+\. (.*?)(?:$|(?=\nTSK \d+\. ))", response, re.DOTALL
        ):
            if not instruction.strip() or await instructor.is_too_similar(
                instruction, min_score=min_score
            ):
                continue
            instructions.append(instruction)
            futures.append(
                instructor.generate_response(
                    instruction, messages=kwargs.get("messages", []), **api_params
                )
            )
        if not futures:
            continue
        responses = await asyncio.gather(*futures)
        for idx in range(len(futures)):
            response = responses[idx]
            if not response or not response.strip():
                continue
            yield {
                "instruction": instructions[idx].strip(),
                "response": response.strip(),
                "category": "general",
            }
            if instructor.instructor_counts["general"] >= target_count:
                break
