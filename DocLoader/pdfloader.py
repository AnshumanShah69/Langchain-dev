from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

loader_instance = PyPDFLoader("sampvalid.pdf")
docs = loader_instance.load()
print(len(docs))

print(docs)
