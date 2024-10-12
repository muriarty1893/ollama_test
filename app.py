import time  
import pdfplumber
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime  

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

template = """
You are an expert job consultant AI. Based on the following document content, provide job recommendations, insights, or potential career paths that could be suitable.

Here is the content of the document:

{pdf_content}

Give your recommendations:
"""

desiredModel = OllamaLLM(model="llama3.2:latest")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | desiredModel

def handle_conv():
    context = ""
    print("Welcome! We'll extract the PDF content and get job suggestions based on it. Type 'exit' to end the conversation.")

    pdf_path = "document.pdf" 
    pdf_content = pdf_to_text(pdf_path)

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

            log_file.write(f"Time: {current_time}\n")
            log_file.write(f"User: {user_input}\n")
            log_file.write(f"Bot: {result}\n")
            log_file.write(f"Response Time: {response_time:.2f} seconds\n\n--------new-chat---------\n")

            context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conv()
