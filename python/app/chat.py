from openai import ChatCompletion


def chat():
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
