from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

parser = StrOutputParser()

class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the text, either positive or negative"
    )

parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(
    template="Get me the sentiment of the following text: {para}\n{format_instructions}",
    input_variables=["para"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classify_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Get me a positive response\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Get me a negative response\n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find the sentiment / neutral")
)

# 🔥 FIX: map feedback → para for classification
input_mapper = RunnableLambda(lambda x: {"para": x["feedback"]})

final_chain = input_mapper | classify_chain | branch_chain

print(final_chain.invoke({"feedback": "I hate this product"}))
