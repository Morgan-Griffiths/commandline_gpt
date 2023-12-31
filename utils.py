import openai
from pymongo import MongoClient
from dtypes import ChatCompletionResponse, Role


def get_gpt_response(prompt):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {"role": "user", "content": f"{prompt}"},
        ],
    )
    parsed_response = ChatCompletionResponse(**response)
    gpt_response = parsed_response.choices[0].message.content
    return gpt_response


def construct_conversation(conversations: list[dict]):
    conversation = ""
    for convo in conversations:
        print('convo',convo, type(convo))
        conversation += "User:\n" + convo['query'] +"\n\nAssistent:\n" + convo['response'] + "\n\n"
    return conversation