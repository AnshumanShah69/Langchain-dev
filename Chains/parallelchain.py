from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

prompt1 = PromptTemplate(
    template="Get me some notes on the following {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Get me some quiz questions on the topic {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="""
Combine the notes and quiz questions into a single paragraph:

Notes:
{notes}

Quiz:
{quiz}
""",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merging_chain = prompt3 | model1 | parser

final_chain = parallel_chain | merging_chain

result = final_chain.invoke({"topic": "Agentic AI"})

print(result)
final_chain.get_graph().print_ascii()
