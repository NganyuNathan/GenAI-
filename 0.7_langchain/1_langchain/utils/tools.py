#tools in here
from langchain_core.tools import tool

@tool
def get_module_deadline(module_name:str)->str:
#any @ is called a python decorator
 """look up the submision deadline for a named bootcamp module
 Args:
  module_name: the name of the module eg "ANN","CNN","RNN"

 """
 deadlines = {
  "ANN":"2023-06-30",
  "CNN":"2023-07-15",
  "RNN":"2023-08-01"
 } 
 return deadlines.get(module_name, "Module not found")

@tool
def count_students_in_module(module_name:str)->str:
     """look up how many students are enrolled in a named bootcamp module"""
     counts = {
         "ANN": 30,
         "CNN": 75,
         "RNN": 100
     }
     return counts.get(module_name, "Module not found")
    

@tool
def pereeqisite_counter(module_name:int)->int:
   """which module must be completed before another""" 

   counter={
        "ANNs":1,
        "CNN":2,
        "RNN":3
   }
   return counter.get(module_name, "Module not found")
#    if module_name not in counter:
#         return "Module not found"
  


@tool
def session_module_lookup(module_name:str)->str:
   """ room/session module lookup"""   

   lookup={
        "ANN":"room 101",
        "CNN":"room 102",
        "RNN":"room 103"
   }
#    if module_name not in lookup:
#         return "Module not found"
   return lookup.get(module_name, "Module not found")