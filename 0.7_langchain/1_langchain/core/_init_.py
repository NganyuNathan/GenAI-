from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system","you are a concise tutor."),
    MessagesPlaceholder("history"),
    ("human", " explain to{input}"),
])
