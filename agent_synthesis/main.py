import os
import queue
import random
import threading
import deepcopy
from getpass import getpass

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

from env import create_env
from converse import create_agent_conversation
from utils import load_queue_from_file, save_queue_to_file, queue_to_dict, save_chats_to_pdf
from env_list import all_environments_description

stop_threads = False
OPENAI_API_KEY = getpass()
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Worker function
def api_worker(args, func, input_queue, output_queue):
    global stop_threads
    while not stop_threads:
        try:
            data = input_queue.get(timeout=1)
            updated_data = func(data, **args)
            output_queue.put(updated_data)
            
            # Mark task as done
            input_queue.task_done()
        except queue.Empty:
            # No more items in queue
            return
        except KeyboardInterrupt:
            print("Received interrupt in worker. Re-queueing item...")
            input_queue.put(data)
            break
        except Exception as e:
            # Handle other exceptions as required
            print(f"Error processing data: {e}")
            input_queue.put(data)  # Re-insert the item into the queue
            
def run(model, all_environments_description, num_threads=4):
    ## Create Environment
    input_queue = queue.Queue()
    output_queue = queue.Queue()

    random.shuffle(all_environments_description)
    for d in all_environments_description:
        input_queue.put(d)
        
    # Launch threads
    threads = []
    stop_threads = False
    args = {"model": model, "num_turns": 1, "apply_critic": False}
    for _ in range(num_threads):
        t = threading.Thread(target=api_worker, args=(args, create_env, input_queue, output_queue))
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt. Signaling threads to terminate...")
        stop_threads = True
        # Now wait for all threads to finish
        for t in threads:
            t.join()
            
    save_queue_to_file(output_queue, "./synthetic/synthetic_environments.pkl")
        
    ## Create Conversation
    input_queue = deepcopy(output_queue)   
    output_queue = queue.Queue()
    
    # Launch threads
    threads = []
    stop_threads = False
    args = {"model": model, "num_turns": 20}
    for _ in range(num_threads):
        t = threading.Thread(target=api_worker, args=(args, create_agent_conversation, input_queue, output_queue))
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt. Signaling threads to terminate...")
        stop_threads = True
        # Now wait for all threads to finish
        for t in threads:
            t.join()
            
    resulting_dicts = queue_to_dict(output_queue)
    save_queue_to_file(output_queue, "./synthetic/synthetic_agent_conversations.pkl")
    save_chats_to_pdf(resulting_dicts, "./synthetic/synthetic_agent_sampler.pdf")

model = ChatOpenAI(model="gpt-4-0613")
model.temperature = 0.8
run(model, all_environments_description, 4)

print("All threads have finished.")

