import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from core.chain import get_chat_chain

st.set_page_config(page_title="Chat", page_icon="🙌")
if "history" not in st.session_state:
    #empty list is going to store the ai message and the human message
    st.session_state.history=[]

chain = get_chat_chain()
# (AiMessage("message"), HumanMessage("message"))
for msg in st.session_state.history:
    role="user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)    
#what if there is an input
user =st.chat_input("Ask your quest")
if user:
    st.session_state.history.append(HumanMessage(content=user)) 
    with st.chat_message("user"):
        st.markdown(user)
    with st.chat_message("assistant"):
        st.spinner("thinking")
        full_reply=st.write_stream(
            chain.stream({"input":user, "history":st.session_state.history[:-1]})

        )  
        with st.spinner("thinking ...."):            
             st.session_state.history.append(AIMessage(content=full_reply))