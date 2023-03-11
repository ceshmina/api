from openai import ChatCompletion
from openai.openai_object import OpenAIObject


def chat() -> OpenAIObject:
    response = ChatCompletion.create(
        model='gpt-3.5-turbo-0301',
        messages=[
            {
                'role': 'user',
                'content': 'こんにちは。'
            }
        ]
    )

    return response
