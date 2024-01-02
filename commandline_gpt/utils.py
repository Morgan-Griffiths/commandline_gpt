from openai import OpenAI
from openai.types.chat import ChatCompletion

client = OpenAI()


def get_gpt_response(prompt):
    MODEL = "gpt-3.5-turbo"
    response: ChatCompletion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {"role": "user", "content": f"{prompt}"},
        ],
    )
    gpt_response = response.choices[0].message.content
    return gpt_response


def construct_conversation(conversations: list[dict]):
    conversation = ""
    for convo in conversations:
        print("convo", convo, type(convo))
        conversation += (
            "User:\n" + convo["query"] + "\n\nAssistent:\n" + convo["response"] + "\n\n"
        )
    return conversation
