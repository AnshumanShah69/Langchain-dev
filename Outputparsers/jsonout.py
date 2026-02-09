from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature=0.3)

parser=JsonOutputParser()
template = PromptTemplate(
    ##parser.get_format_instructions() adds return a json object by default and the template can be used to add more instructions to the model to follow when generating the output
    template="Write about corporate politics in paragraph format \n in {format_instruction}", input_variables=[], partial_variables = {"format_instruction": parser.get_format_instructions()})

chain = template | model | parser

#chain.invoke requires a parameter to be passed in but since we have no input variables in the template we can just pass in an empty dictionary or leave it empty as shown below

#json output parser does not enforce a scehema but it does enforce a json format and the model will try to follow the instructions given in the template to generate a json output that can be parsed by the JsonOutputParser. If the model fails to generate a valid json output, the parser will raise an error.
result = chain.invoke({})
print(result)