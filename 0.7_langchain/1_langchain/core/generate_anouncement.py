from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN
from .chain import anouncement_chain
from .prompts import prompt

model=create_model(QWEN)

result=anouncement_chain.invoke({
    "tone":"low tone",
    "audience":"developers",
    "announcement_details":""
})

class announcement(BaseModel):
    tone:str=Field(description="{result}")
    anouncement_details:str=Field(description="{result}")  

class details(result): 
         title:str=Field(description="welcome to seed all those who have punishments should own up ") 
         audience:str=Field(description="all interns ")  
         tone:str=Field(description="medium tone ")
         message:str=Field(description="all interns are to be at the site at 9am ")  
class tone(result):
           title:str=Field(description="welcome to seed all those who have punishments should own up ") 
           audience:str=Field(description="all interns ")  
           tone:str=Field(description="low tone ")
           message:str=Field(description="all interns are to be at the site at 9am ")  



structured_model = model.with_structured_output(announcement)
results = structured_model.invoke("{prompt}")
print(results.model_dump())