from langchain_ollama import OllamaLLM

model = OllamaLLM(model = "llama3.2:latest")

result = model.invoke(input="write a poem in the style of bukowski about hating flies")

print(result)