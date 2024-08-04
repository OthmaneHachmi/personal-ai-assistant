import os
from dotenv import load_dotenv
from groq import Groq

#load the environment variables
load_dotenv()

class PersonalAssistant:
    
    def __init__(self):
        #Define the model
        self.model = "mixtral-8x7b-32768"
        #Get the api key from the environment variables
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
    
    def text_genertion(self, prompt):    
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        text = chat_completion.choices[0].message.content
        return text
    