from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature=0.5)


class SummaryWorker(TypedDict):
    summary: str

structured_model = model.with_structured_output(SummaryWorker)

result = structured_model.invoke("the mouse is great but lacks quality and durability")

print(result)