from langchain_core.tools import tool
import urllib.parse
import requests
import os

@tool
def generate_image(prompt:str)->str:
    """
    Generate an image from a text description and return the file path.
    use this when the user asks you to create, draw, or visualise something.
    Args:
    prompt: A clear, descriptive prompt of the image to generate
    
    """
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024"
    response=requests.get(url, timeout=60)
    response.raise_for_status()
    os.makedirs("generated_images", exixt_ok=True)
    path=f"generated_images/{abs(hash(prompt))}.png)"

    #to write or place the image in that path
    with open(path, 'wb') as f:
        f.write(response.content)
    return path