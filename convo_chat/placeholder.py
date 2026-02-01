from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create chat prompt template
chat_temp = ChatPromptTemplate.from_messages([
    ("system", "You are a subscription advisor."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}")
])

# Load chat history
chat_history = []

with open("history.txt") as f:
    for line in f:
        chat_history.append(("human", line.strip()))

# Debug
print(chat_history)

# Invoke prompt
prompt = chat_temp.invoke({
    "history": chat_history,
    "query": "Is my subscription active?"
})
