import queue
from tqdm import tqdm

from langchain.schema import HumanMessage


ENVIRONMENT_PROMPT_TEMPLATE = \
'''
You will simulate a software environment that can be used by a user or agent. You will simulate the following software environment:
{}

The following information explains the expectations about inputs and outputs of the environment:
{}

You should do your absolute best to interact with the user as if you are the given environment. You should NOT act as if you are chatGPT, GPT-4, or any other AI agent. The goal is to make a convincing simulation. Below you are given information about the state of the environment:
{}

When acting as the environment, you may make up any data or information you need, as long as it is consistent with the state and the user actions. You should prefer realistic data and responses over “example” data that is generic (“Matthew Harris” is better than “John Doe”, “Carter Products” is better than “Acme Products”). Your outputs should ALWAYS be consistent with the expectations about outputs!

In any situation where the inputs from the user are incomplete, unrecognized, or not as per the expected format for the software environment, you should return an error and generic information about how inputs of the given type may be presented. 

Please start with an opening message from the software environment to the user with a basic explanation of how to begin using the software environment.
'''

AGENT_PROMPT_TEMPLATE = \
'''
Interact with a software environment to solve a task. Imagine you are an intelligent agent working for a user and your target is to perform actions to complete the task goal. At the beginning of your interactions, you will be given a detailed description of the current environment and your goal to accomplish. For each of your turns, you will be given a list of actions which you can choose one to perform in this turn. You should provide two parts of your response: "THOUGHT" and "ACTION". For  "THOUGHT", you should first think about the current condition and plan for your future actions, and then output your "ACTION" in this turn. Your output must strictly follow this format:"THOUGHT: your thoughts.
 ACTION: your next action 
"; For "ACTION", you should directly output the action this turn. Your output must strictly follow this format:"ACTION: your next action
". After your each turn, the environment will respond based on your actions which you may use to plan your next few steps. if the environment output includes an error, that means the previous action is invalid and you should try more options. If you have finished the task, you can call the success function "success([outputs,...])" with any final outputs.
 Reminder: 
1. the action must follow any formats requested
2. Think when necessary, try to act directly more in the process.
If information is requested that you don't have, you may use placeholder information, but please note the information when calling "success()". You may use information you are aware of to help solve the task, but you should not attempt to solve the task without using the software environment. 

Software Environment: {}
Your Task: {}
'''

def create_agent_conversation(tasks, model, num_turns=20): 
    for i in tqdm(range(len(tasks)), desc="running agent interactions"):
        environment_prompt = ENVIRONMENT_PROMPT_TEMPLATE.format(tasks[i]['environment'], tasks[i]['io'], tasks[i]['state'])
        agent_prompt = AGENT_PROMPT_TEMPLATE.format(tasks[i]['environment'], tasks[i]['task'])
        agent_messages = [
            HumanMessage(content=agent_prompt),
        ]

        environment_messages = [
            HumanMessage(content=environment_prompt)
        ]

        for _ in range(num_turns):
            environment_result = model.predict_messages(environment_messages)
            print('Env:', environment_result)
            environment_messages.append(environment_result)
            agent_messages.append(HumanMessage(content=environment_result.content))
            agent_response = model.predict_messages(agent_messages)
            agent_result = agent_response.content.split("ACTION:")[1].strip()
            environment_messages.append(HumanMessage(content=agent_result))
            agent_messages.append(agent_response)
            print('Agent:', agent_result)
            if "success(" in agent_result:
                break
        tasks[i]["conversation"] = agent_messages
    print('tasks =', tasks)
    return tasks