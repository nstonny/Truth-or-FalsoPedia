#include imports

class AI_service:

    def __init__(self):
        """
        1. define model, max_tokens, temperature
        2. initialize the model: openai client
        """
        pass

    def generate_statements(self, title: str, summary: str):
        #Asks OpenAI to produce one true and one false statement about an article.
        pass

    def build_prompt(self, title: str, summary: str):
        #Constructs the prompt sent to OpenAI.
        pass

    def parse_response(self, raw_text: str) :
        #Parses and validates the JSON string returned by OpenAI.
        pass