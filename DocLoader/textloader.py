from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

#Model creation
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.1)

#Prompt
prompt = PromptTemplate(template = "Summarize about {typeofgame} game and get me which type of game are we talking about and get me the answer in just a word, the type of game", input_variables=["typeofgame"])

#Parser
parser = StrOutputParser()

loader_instance = TextLoader("sampletxt.txt", encoding="utf-8")
 
docs = loader_instance.load()
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
print("----")
chain = prompt | model | parser

print(chain.invoke({"typeofgame": docs[0].page_content}))