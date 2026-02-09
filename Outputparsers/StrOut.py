from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# 1st prompt
T1 = PromptTemplate(
    template="Write about corporate {topic}",
    input_variables=["topic"]
)

# 2nd prompt
T2 = PromptTemplate(
    template="Write a joke about {text}",
    input_variables=["text"]
)

# parser
parser = StrOutputParser()

# chain pipeline
chain = T1 | model | parser | T2 | model | parser

### in step 3 the parser automatically takes the text and sends it to the T2 parameter text and automaticaly sends the things to the model for processing and to the final parser stage 
result = chain.invoke({"topic": "corporate"})
print(result)
