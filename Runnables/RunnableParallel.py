from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

#Model preparation
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.3)

#Parser preparation
parser = StrOutputParser()

#Prompt1
prompt1 = PromptTemplate(template = "Get me some information about {AI}", input_variables = ["AI"])

#Prompt2
prompt2 = PromptTemplate(template = "Get me some information about {ML}", input_variables = ["ML"])

parallelrunnable = RunnableParallel({
    "AI":(prompt1 | model | parser),
    "ML":(prompt2 | model | parser),
})

result = parallelrunnable.invoke({"AI": "Langchain", "ML": "Random Forest"})

print(result["AI"])
print(result["ML"])  