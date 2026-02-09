from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", task = "text_generation", temperature=0.3)

# Define the Pydantic model for the output
class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age", gt = 20, lt = 100)
    city: str = Field(description="The city where the person lives")

# Create the PydanticOutputParser
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(template="Get me a biography of a person {designation} and {place} \n {format_instructions}", input_variables=["designation", "place"], partial_variables={"format_instructions": parser.get_format_instructions()})

prompt = template.format(designation="software engineer", place="San Francisco")
response = model.invoke(prompt)

result = parser.parse(response.content)
print(result)