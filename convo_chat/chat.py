from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

chat_memory = []

while(1):
    user_prompt = input("Enter your prompt (type 'quit' to exit): ")
    chat_memory.append(user_prompt)
    if user_prompt.lower() == "quit":
        break
    response = model.invoke(chat_memory)
    chat_memory.append(response.content)
    print("AI: " + response.content)
print(chat_memory)