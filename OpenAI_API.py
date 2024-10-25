from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json


class CarPartsPricesOpenAI:

    def __init__(self, model_name="gpt-3.5-turbo-1106"):
        self.api_key = 'your api key'
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=.3,
            max_tokens=None,
            timeout=None,
            max_retries=3,
            api_key = self.api_key,
        )
        messages = [
    (
        "system", """You are an AI agent tasked with generating the price in dollars for specific car parts based on the given input dictionary.
        
        => The input is a dictionary where each key is an index, and the value is a string formatted as 'Brand & Model & Part_name'.
        => The expected output is a JSON dictionary where each key matches the input key, but the value is the price of the car part in dollars. The output should only contain the price as a number (e.g., 10), not with a dollar sign or any additional formatting (e.g., '10$' is incorrect).
        => Ensure you provide realistic prices for the car parts based on the type of part and the vehicle model, without generating random or placeholder data.
        => Always maintain consistency in the price estimation logic for similar parts and models.
        """
    ),
    (
        "human", """Generate a JSON dictionary where the keys match the given input dictionary, and the values are the corresponding prices for the car parts in dollars. The prices should be provided as plain numbers, without any currency symbol or formatting. Here is the input dictionary:
        
        {car_parts_data}
        """
    )
]

        
        self.json_llm = self.llm.bind(response_format={"type": "json_object"})
        self.template = ChatPromptTemplate.from_messages(messages)
        self.chain = self.template | self.json_llm
        
    def predict(self, car_parts_data):
        ai_msg = self.chain.invoke({'car_parts_data':car_parts_data})
        results = {}
        results['content'] = json.loads(ai_msg.content)
        results['completion_tokens'] = ai_msg.response_metadata['token_usage']['completion_tokens']
        results['prompt_tokens'] = ai_msg.response_metadata['token_usage']['prompt_tokens']
        results['total_tokens'] = ai_msg.response_metadata['token_usage']['total_tokens']
        results['model_name'] = ai_msg.response_metadata['model_name']
        return results