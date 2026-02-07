from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)

st.header("Gemini based document summarizer")

topic = st.selectbox(
    "Select topic of summary:",
    ["Business", "Technology", "Health", "Education", "Entertainment"]
)

style = st.selectbox(
    "Select style of summary:",
    ["Concise", "Detailed", "Bullet Points", "Narrative", "Technical"]
)

length = st.selectbox(
    "Select length of summary:",
    ["Short-5 lines", "Medium-10 lines", "Long-15 lines"]
)

# ✅ PromptTemplate (THIS WAS MISSING)

template = load_prompt("template.json")

if st.button("Generate Summary"):

    #basically we are requesting template and model, then we are passing the parameters to the invoke method to complete the template then we are calling the model and then printing the result    

    #1 invoke method instead of 2 calls - model.invoke and template are not called instead we use chains.invoke which is a combination of both template and model.
    chains = template | model # Create a chain by piping the prompt to the model
    result = chains.invoke({
        "style": style,
        "length": length,
        "topic": topic
    }) 
    st.write(result.content)
