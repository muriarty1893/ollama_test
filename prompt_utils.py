from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def create_prompt_chain():
    template = """
    You are an expert job consultant AI. Based on the following document content, provide job recommendations, insights, or potential career paths that could be suitable.

    Here is the content of the document:

    {pdf_content}

    Give your recommendations:
    """
    desiredModel = OllamaLLM(model="llama3.2:latest")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | desiredModel
    return chain
