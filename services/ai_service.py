#include imports
import os
from dotenv import load_dotenv
from category.single_category import Category
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI

client = OpenAI(api_key=api_key)


class AI_service:

    def __init__(self, user_category):
        """
        1. define model, max_tokens, temperature
        2. initialize the model: openai client
        """
        self.user_category = user_category


    def generate_statements(self):
        #Asks OpenAI to produce one true and one false statement about an article.

        # single category

        category = Category(self.user_category)
        print(self.user_category)
        summaries = category.get_summary()

        # creating the prompt for openAI
        prompt = self.build_prompt(summaries)

        """

        try:
            # to openAI
            response = client.responses.create(
            model="gpt-5-nano",
            input= prompt,
            )

            # parsing the response from openAI
            parse_response = self.parse_response(response.output_text)
            return parse_response
        except Exception as e:
            print("Something went wrong:", e)"""


    def build_prompt(self, summaries: str):
        #Constructs the prompt sent to OpenAI.
        prompt = f"""You are helping create a quiz game based on Wikipedia articles.

        Here is a list of Wikipedia article summaries:
        Summaries: {summaries}

        For each summary in the list, your task is to:
        1. Write ONE statement that is TRUE and accurately reflects the summary.
        2. Write ONE statement that is FALSE but sounds plausible — it should be tricky!

        Respond ONLY with a valid JSON list in this exact format:

        [
          {{"true_statement": "Your true statement here", "false_statement": "Your false statement here."}},
          {{"true_statement": "Your true statement here", "false_statement": "Your false statement here."}},
          {{"true_statement": "Your true statement here", "false_statement": "Your false statement here."}}
        ]
        """

        return prompt

    def parse_response(self, raw_text: str) :
        #Parses and validates the JSON string returned by OpenAI.
        statements = json.loads(raw_text)
        return statements
