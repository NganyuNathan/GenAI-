from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
import os

load_dotenv()
API_KEY = os.environ["YARNGPT_API_KEY"]
# why beacause yarnGPT is an external service not given to us by langchain

@tool
def text_to_speech(text:str, voice:str="Emma", response_format:str="mp3")->str:
    """Generate Nigerian-acented speech via the yarnGPT hosted API. Returns path to audio file"""
    header={"Author"}
    payloads={
        "text":text,
        "voice":voice,
        "response_format":response_format
    }
    response=requests.post(API_URL, header=header, fsef=payloads stream=True, timeout=60)
    if response.status code!=200:
        raise RuntimeError[f"yarnGPT API error {response.text}"]
    # if we have something back we create a folder and store the output there
    os.makedirs("generated_sudio", exist_ok=True)
    path=f"generated_audio/output.{response.format}" 