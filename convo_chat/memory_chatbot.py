from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
chat_memory = [SystemMessage(content="You are a helpful salesman AI chatbot.")]

while(1):
    user_prompt = input("User: ")
    chat_memory.append(HumanMessage(content=user_prompt))
    response = model.invoke(chat_memory)
    chat_memory.append(AIMessage(content=response.content))
    print("AI: " + response.content)
print(chat_memory)