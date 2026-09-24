from langchain.agents import create_agent
from .models import create_model
from utils.tools import get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup

model = create_model()

# agent = create_agent(
#     model = model,
#     tools=[get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup],
#     system_prompt = "you are a helpful assistant that can answer questions about modules, students, and sessions. You have access to the following tools: get_module_deadline, count_students_in_module, pereeqisite_counter, session_module_lookup. Use these tools to provide accurate and relevant information to the user."

# )
# # result = agent.invoke({"messages":[{"role":"user","content":"When is the CNN module due?"}]})
# # print(result["messages"][-1]["content"])

# for step in agent.stream({"messages":[{"role":"user","content":"When is the ANN module due?"}]}):
#   print(step)


agent = create_agent(
    model = model,
    tools=[get_module_deadline, count_students_in_module,pereeqisite_counter,session_module_lookup],
    system_prompt = "you are a model that can answer questions"
)