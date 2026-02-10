from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(template = "Get me 5 lines on {Technology}", input_variables = ["Technology"])

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({"Technology": "Artificial Intelligence"})
print(response)

chain.get_graph().print_ascii()