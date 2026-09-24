from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate([
    option = st.selectbox(("system","you are a concise chef in cooking food ai assistant, answer in max sentences", 
                           "you are a concise tutor, answer in max sentences", 
                           "you are a concise medical assistant, answer in max sentences"),
                           )
    (MessagesPlaceholder("history")),
    ("human", "{input}")
])
