from .models import create_model
from config import QWEN

model = create_model(QWEN)
response = model.invoke("who is the ceo of anthropic")
print(response.content)

# for chunk in model.stream("who is bill gates"):
#     print(f"{chunk.content}", end="|", flush=True)

# message_batch
message_batch=[
    "why do they call black american Nigros"
    "Who was the firat president of cameroon"
    "Who started the first World war 2?"

]
response=model.batch(message_batch)
for r in response:
    print(r.text)