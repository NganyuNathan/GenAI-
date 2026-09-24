from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN

model=create_model()

#create the blueprint for the output of the model
class Player(BaseModel):
    name:str=Field(description="Name of palyer")
    age:int=Field(description="Age of player")
    nationality:int=Field(description="Nationality of player")
    flag:int=Field(description="Flag of player")
class top(BaseModel):
    opinion:str=Field(description="opinion of the top 10 players ") 
    players:list[Player]=Field(description="List of the top 10 footballers of all time")    

structured_model = model.with_structured_output(top)
result = structured_model.invoke("give me the best 10 footballers of all time")
print(result.model_dump())