from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough

load_dotenv()

#prompt preparation
prompt = PromptTemplate(template = "Get me something on {cars} Company", input_variables = ["cars"])

prompt2 = PromptTemplate(template = "Summarize about the {companyhistory}", input_variables = ["companyhistory"])

#Model preparation
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.3)

#Parser preparation
parser = StrOutputParser()

report_gen = RunnableSequence(prompt | model | parser)
#or prompt | model | parser only also correct
branch = RunnableBranch(
    (lambda x: len(x.split()) > 5, RunnableSequence(prompt2 | model | parser)),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen |  branch)

result = final_chain.invoke({"cars": "Tesla"})
print(result)