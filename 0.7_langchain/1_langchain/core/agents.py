# from langchain.agents import create_agent
# from .models import create_model
# from utils.tools import get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup

# model = create_model()

# agent = create_agent(
#     model = model,
#     tools=[get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup],
#     system_prompt = "you are a helpful assistant that can answer questions about modules, students, and sessions. You have access to the following tools: get_module_deadline, count_students_in_module, pereeqisite_counter, session_module_lookup. Use these tools to provide accurate and relevant information to the user."

# )
# # result = agent.invoke({"messages":[{"role":"user","content":"When is the CNN module due?"}]})
# # print(result["messages"][-1]["content"])

# for step in agent.stream({"messages":[{"role":"user","content":"When is the ANN module due?"}]}):
#   print(step)


# agent = create_agent(
#     model = model,
#     tools=[get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup],
#     system_prompt = "you are a model that can answer questions"
# )
from langgraph.prebuilt import create_react_agent
from core.models import create_model
# from tools.image_analysis import analyse_image
from tools.image_gen import generate_image
from tools.voice import text_to_speech
from tools.web_search import web_search
# import streamlit as st

SYSTEM_PROMPT = """ you are a helpful multimodal assistant with tools for image analysis, image generation, websearch, and text-to-speech.
Only call a tool when the request genuinely needs it:
-analyse_image:only when the image has been uploaded and the user is asking about it.
-generate_image:only when the user explicitely ask you to create, draw, or visualise something.
-web_search: only for current events, recent news, or facts you wouldent reliably know.
-text_to_speech: only when the user explicitly asks for anaudio output.

For everthing else, greetings, general knowledge, explanations, conversations, answer dire without calling any tool.
"""

# @st.cache_resource
def build_multimodal_agents():
    model = create_model()
    tools = [generate_image,web_search,text_to_speech]
    return create_react_agent(model, tools, prompt=SYSTEM_PROMPT)

# image = build_multimodal_agents()


# result = image.invoke({
#     "message":[{"role":"user","content":"generate an image of jose mourinho"}]
# })