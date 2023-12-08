'''
This file contains the SubliminalGenerator class responsible for generating subliminal messages based on user inputs.
'''
import openai
class SubliminalGenerator:
    def __init__(self, api_key):
        # Initialize OpenAI API
        openai.api_key = api_key
    def generate_subliminal(self, prompt, waves, music):
        # Generate subliminal message using GPT prompt and user inputs
        input_text = f"{prompt}\nWaves: {', '.join(waves)}\nMusic: {music}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=100,
            temperature=0.7
        )
        subliminal_message = response.choices[0].text.strip()
        return subliminal_message