from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()

#Prompt Template
prompt = PromptTemplate(template = "Get me a reality fact about {corporate}", input_variables = ["corporate"])

#Model preparation
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.3)

#Parser preparation
parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

#Similarly we can add more steps in the cahins with prompt 2
result = chain.invoke({"corporate": "People in corporate world"})

print(result)