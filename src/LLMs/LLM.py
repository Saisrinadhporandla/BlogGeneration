from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv




class ModelClass():
    def __init__(self):
        load_dotenv()
        self.api_key=os.getenv("GROQ_API_KEY")

    def load_llm(self):
        try:
            model=ChatGroq(model="openai/gpt-oss-120b",api_key=self.api_key)
            return model
        except Exception as e:
            raise ValueError(e)


