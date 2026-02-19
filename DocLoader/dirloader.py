from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

loader = DirectoryLoader(
    path = "pdfs",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(docs)