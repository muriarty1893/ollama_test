from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime  # Tarih ve saat eklemek için

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

desiredModel = OllamaLLM(model="llama3.2:latest")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | desiredModel

def handle_conv():
    context = ""
    print("Welcome to the conversation! Type 'exit' to end the conversation")

    # Dosyayı aç (varsa üzerine yazar, yoksa yeni oluşturur)
    with open("conversation_log.txt", "a") as log_file:
        while True:
            user_input = input("""-----------------------------------
You: """)
            if user_input.lower() == "exit" or user_input.lower() == "q":
                break
            
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot: ", result)
            
            # Tarih ve saat bilgisi al
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Terminal çıktısını dosyaya kaydet (tarih ve saat ile birlikte)
            log_file.write(f"Time: {current_time}\n")
            log_file.write(f"User: {user_input}\n")
            log_file.write(f"Bot: {result}\n\n--------new-chat---------\n")
            
            # Konuşma geçmişini güncelle
            context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conv()
