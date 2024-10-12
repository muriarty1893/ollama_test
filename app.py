from pdf_utils.pdf_processing import pdf_to_text
from prompt_utils.prompt_chain import create_prompt_chain
from log_utils.logging import log_conversation
from datetime import datetime
import time

def handle_conv():
    print("Welcome! We'll extract the PDF content and get job suggestions based on it. Type 'exit' to end the conversation.")
    pdf_path = "document.pdf" 
    pdf_content = pdf_to_text(pdf_path)
    chain = create_prompt_chain()

    with open("conversation_log.txt", "a") as log_file:
        while True:
            user_input = input("""-----------------------------------
You: """)
            if user_input.lower() == "exit" or user_input.lower() == "q":
                break

            start_time = time.time()
            
            result = chain.invoke({"pdf_content": pdf_content})

            end_time = time.time()
            response_time = end_time - start_time 

            print(f"Bot: {result}")
            print(f"Response Time: {response_time:.2f} seconds")  

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_conversation(log_file, current_time, user_input, result, response_time)

if __name__ == "__main__":
    handle_conv()
