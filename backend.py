import openai

API_KEY = "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"


class Chatbot:
    def __init__(self):
        # openai.api_key = "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"
        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write me a joke about windows")
    print(response)
