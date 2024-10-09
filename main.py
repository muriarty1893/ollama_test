from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
Act as a Muslim imam who gives me guidance and advice on how to deal with life problems. 
Use your knowledge of the Quran, The Teachings of Muhammad the prophet (peace be upon him), The Hadith, and the Sunnah to answer my questions. 
Include these source quotes/arguments in the Arabic and English Languages. 
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model = "llama3.2:latest")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conv():
    context=""
    print("Welcome to the conversation! type 'exit' to end the conversation")
    while True:
        user_input = input("""-----------------------------------
You: """)
        if user_input.lower() == "exit":
            break
        
        result = chain.invoke({"context":context,"question":user_input})
        print("Bot: ",result)
        context+= f"\nUser: {user_input}\nAI: {result}"
    
if __name__ == "__main__":
    handle_conv()