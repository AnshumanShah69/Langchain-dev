from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, TypedDict, Annotated, Literal
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

#this is json schema

json_schema = {
    "title": "Mobile Review Summary",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List all the key points of a mobile that was described"
        },
        "summary": {
            "type": "string",
            "description": "A concise summary of the mobile's features and specifications"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The overall sentiment of the review, which can be positive, negative, or neutral"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of the advantages or positive aspects of the mobile"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of the disadvantages or negative aspects of the mobile"
        },
        "name_of_author": {
            "type": ["string", "null"],
            "description": "The name of the author of the review, if available"
        }
    },
}

structured_data = model.with_structured_output(json_schema)

# here we are sending the prompt to the model and it will return the output in the form of our pydantic class which we can easily convert to a dictionary or json as per our requirement. This is the power of using pydantic with langchain, it allows us to have a structured output which is easy to work with and also provides validation for our data.
result = structured_data.invoke("""Summarize the following review of a mobile phone, extracting key themes, a concise summary, sentiment, pros and cons, and the name of the author if available: 'The new XYZ smartphone has a bad display and bad battery life. it lacks a good camera and the user interface and can be sluggish at times. Overall, it's a bad phone for its price.'""")

print(result["name_of_author"])