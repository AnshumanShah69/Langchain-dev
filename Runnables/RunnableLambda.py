from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

load_dotenv()

def wordcounting(text):
    return len(text.split())

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.0
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate a haiku for {workplace}",
    input_variables=["workplace"]
)

haiku_gen = prompt | model | parser

parallelchains = RunnableParallel({
    "haiku": lambda x: x,  # passthrough output
    "word_count": RunnableLambda(wordcounting)
})

final_chain = haiku_gen | parallelchains

result = final_chain.invoke({"workplace": "samurai"})

print(result["haiku"])
print(result["word_count"])
