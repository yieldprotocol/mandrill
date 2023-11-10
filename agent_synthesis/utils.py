import html
import pdfkit
import pickle
import queue
import random
import threading
from langchain.schema import HumanMessage

def save_chats_to_pdf(list_of_chat_histories, filename):
    combined_html = ""
    for chat_history in list_of_chat_histories:
        combined_html += format_single_chat(chat_history)
    
    # Generate PDF from the combined HTML content
    pdfkit.from_string(combined_html, filename)
    
def save_queue_to_file(q, filename):
    with open(filename, 'wb') as file:
        pickle.dump(list(q.queue), file)

def load_queue_from_file(filename):
    try:
        q = queue.Queue()
        with open(filename, 'rb') as file:
            the_list = pickle.load(file)
            for item in the_list:
                q.put(item)
        return q
    except (FileNotFoundError, EOFError):
        return queue.Queue()
    
def format_single_chat(chat_data):
    # Use a function to replace newlines with <br> tags
    def format_text(text):
        return html.escape(text).replace('\n', '<br>')

    # Start the HTML string
    formatted_html = '<div style="border: 1px solid #ddd; padding: 10px; max-width: 1000px; margin-bottom: 20px;">'
    
    # Add the task description as a header before the conversation starts
    formatted_html += f'<h2>{format_text(chat_data["task"])}</h2>'

    # Add environment, io, state, and task at the beginning with smaller font and neutral background
    formatted_html += f'<div style="background-color: #f5f5f5; padding: 10px; font-size: 0.9em;">'
    formatted_html += f'<strong>Environment:</strong> {format_text(chat_data["environment"])}<br>'
    formatted_html += f'<strong>IO:</strong> {format_text(chat_data["io"])}<br>'
    formatted_html += f'<strong>State:</strong> {format_text(chat_data["state"])}<br>'
    formatted_html += '</div>'
    
    # Go through each message in the conversation
    for message in chat_data["conversation"]:
        # Determine message source and set appropriate color
        if isinstance(message, HumanMessage):
            color = "#d9e3f0"  # Light blue for human
            from_who = "Human"
        else:  # AIMessage
            color = "#e1d4e1"  # Purple for AI
            from_who = "AI"
        
        # Format the message with a slightly larger padding and rounded corners
        formatted_html += f'<div style="background-color: {color}; padding: 20px; border-radius: 5px; margin: 20px 0;">'
        formatted_html += f'<strong>{from_who}:</strong> <div style="margin-top: 5px;">{format_text(message.content)}</div>'
        formatted_html += '</div>'
    
    # Close the main div
    formatted_html += '</div>'
    
    return formatted_html

def queue_to_dict(output_queue):
    resulting_dicts = []
    while not output_queue.empty():
        resulting_dicts.append(output_queue.get())
    return resulting_dicts