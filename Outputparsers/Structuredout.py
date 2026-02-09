from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

schema = [
    ResponseSchema(name="universal_truths_1", description="Universal Fact 1"),
    ResponseSchema(name="universal_truths_2", description="Universal Fact 2"),
    ResponseSchema(name="universal_truths_3", description="Universal Fact 3"),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate.from_template(
    "List 3 universal truths about the {topic}\n. {format_instructions}", input_variables = ["topic"], partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format(topic="universe")
response = model.invoke(prompt)

finalresult = parser.parse(response.content)
print(finalresult)
