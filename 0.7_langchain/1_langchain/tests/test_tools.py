from tools.image_gen import generate_image
from tools.voice import text_to_speech

result= generate_image.invoke({"prompt":"a boy riding a bycicle"})
print(result)

# path = text_to_speech("welcome to this amazing course, very angry to create this tool")
# print(path)

# image = generate_image()

# result = image.invoke({
#         "messages":[{"user":"generate an image of billgates"}]
# })
# print(result["messages"][-1].content)