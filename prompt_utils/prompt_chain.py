from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def create_prompt_chain():
    template = """
    You are an expert at C++ and you are going to write a windows desktop app in C++ language. I will gice you pdf of a book that my teacher wrote. Its about ICBYTES library in C++ that my teacher wrote. Here's what is the app about;do a animation that at least 3 seconds, there will be multiple objects that  move in different speed and at the same time. Also therell be a start button for me to start the animation.

    Here is the content of the document for you to learn ICBYTES library:

    {pdf_content}

    Now write the code:
    """
    desiredModel = OllamaLLM(model="llama3.2:latest")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | desiredModel
    return chain
