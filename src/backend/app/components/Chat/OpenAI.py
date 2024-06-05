from langchain_openai import ChatOpenAI
from app.components.Chat.Base import AbstractLLMComponent

class ChatOpenAIComponent(AbstractLLMComponent):
    def __init__(self, openai_api_key):
        super().__init__()
        self.openai_api_key = openai_api_key

    def configure(self, temperature=0.7):
        self.model_instance = ChatOpenAI(api_key=self.openai_api_key, temperature=temperature)

    def execute(self, prompt):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        response = self.model_instance.invoke(prompt)
        return response.content
