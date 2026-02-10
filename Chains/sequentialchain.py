from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(template = "Get me a detailed paragraph on {Technology}", input_variables = ["Technology"])

prompt2 = PromptTemplate(template = "Get me the most important 2 lines from the {paragraph}", input_variables = ["paragraph"])

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"Technology": "Machine learning"})

print(result)

chain.get_graph().print_ascii()