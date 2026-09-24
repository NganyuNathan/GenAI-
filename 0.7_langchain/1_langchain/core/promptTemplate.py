from .models import create_model
from config import QWEN
# we are going to be using something called: chatprompt to create to prompt template
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# a good example of a prompt template
#describe this {football_payer} in one sentence

model = create_model(QWEN)
parser = StrOutputParser()

# prompt_template=ChatPromptTemplate.from_message(
#     [
#     #system message: "a message given the the model in other for it to determine how to rspond to a user"
#     ("system", "please in one sentence who is the best midfilder in premeir leauge history and give a list of his achievements"),
#     ("human","{question}")
#     ]

# football_player=input("enter the name of the player")
# question=input("enter question")

# chain=prompt_template | model
# #to use this prompttemplate we use the invoke method:
# result=chain.invoke({
#     "football_player":football_player
#     "question":question
# })
# print(result)
# )

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a concise medical assistant, answer in max{max_sentence} sentences"),
    ("human", "{question}")
])
chain = prompt|model|parser
result=chain.invoke({
    "max_sentence": 5,
    "question":"what is the differnce between high blood and low blood pressure"
})
print(result)