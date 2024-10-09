import ollama

desiredModel='llama3.2:latest'
questionToAsk='What is the capital of France?'

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'system',
        'content': questionToAsk,
    },
])