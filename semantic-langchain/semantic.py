from operator import index
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embed = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions=300)

document = [
    "LangChain is a framework for developing applications powered by language models.",
    "It enables developers to build applications that can understand and generate human-like text.",
    "LangChain provides tools for prompt management, memory, and integration with various data sources.",
    "India is known for its diverse culture and rich history."
]
user_query = "tell me about india??"

document_embeddings = embed.embed_documents(document)
query_embedding = embed.embed_query(user_query)
#here we just want the single list not the entire nested list so 0 th index is used
score = cosine_similarity([query_embedding], document_embeddings)[0]

#we have to sort these scores but the thing is it will mix the original sequence, instead we will put in enumerate to keep track of original index
#after sorting we will get the last element which will have the highest score from the last using -1 index
index,score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

#printing the document index and its similarity score
print(document[index])
print("Similarity score : " + str(score))

load_dotenv()
