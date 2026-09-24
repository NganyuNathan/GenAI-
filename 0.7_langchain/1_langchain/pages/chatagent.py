import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage
from core.agents import build_multimodal_agents


st.set_page_config(page_title="BambiGPT",page_icon="👀")

if "history" not in st.session_state:
    st.session_state.history = []

st.header("BambiGPT 👀🥶")

chain = build_multimodal_agents()

for msg in st.session_state.history:

    role = "user" if isinstance(msg, HumanMessage) else "assistant"

    with st.chat_message(role):
        st.markdown(msg.content)
user = st.chat_input("Ask any question 👮")
if user:

    human_message = HumanMessage(content=user)
    st.session_state.history.append(human_message)

    with st.chat_message("user"):
        st.markdown(user)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = chain.invoke({"messages": st.session_state.history})
            answer = response["messages"][-1].text

            st.markdown(answer)

    st.session_state.history.append(AIMessage(content=answer))