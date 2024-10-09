import ollama

desiredModel='llama3.2:latest'
questionToAsk='write a poem in the style of bukowski about hating flies'

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': questionToAsk,
    },
])

OllamaResponse = response['message']['content']

print(OllamaResponse)

with open('OutputOllama.txt', 'w', encoding="utf-8") as text_file:
    text_file.write(OllamaResponse)