from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    ("system","You are a {domain} expert."),
    ("human","Explain me in bullet points about {topic}.")
)

prompt = chat_template.invoke({"domain":"technology","topic":"AI"})
print(prompt)