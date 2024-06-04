import openai
import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class BaseModelService:
    def __init__(self, api_key: str, api_endpoint: str):
        self.api_key = api_key
        self.api_endpoint = api_endpoint

    def _get_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _fetch_models(self) -> Optional[dict]:
        response = requests.get(self.api_endpoint, headers=self._get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch models: {response.status_code}")

class OpenAIService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("OPENAI_API_KEY"), api_endpoint=os.getenv("OPENAI_API_ENDPOINT"))

    def get_models(self):
        openai.api_key = self.api_key
        response = openai.models.list()
        return list(response)

class OllamaService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("OLLAMA_API_KEY"), api_endpoint=os.getenv("OLLAMA_API_ENDPOINT"))

    def get_models(self):
        return self._fetch_models()

class AnthropicService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("ANTHROPIC_API_KEY"), api_endpoint=os.getenv("ANTHROPIC_API_ENDPOINT"))

    def get_models(self):
        return self._fetch_models()

class AL21LabsService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("AL21LABS_API_KEY"), api_endpoint=os.getenv("AL21LABS_API_ENDPOINT"))

    def get_models(self):
        return self._fetch_models()

class CohereService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("COHERE_API_KEY"), api_endpoint=os.getenv("COHERE_API_ENDPOINT"))

    def get_models(self):
        return self._fetch_models()

class TitanService(BaseModelService):
    def __init__(self):
        super().__init__(api_key=os.getenv("TITAN_API_KEY"), api_endpoint=os.getenv("TITAN_API_ENDPOINT"))

    def get_models(self):
        return self._fetch_models()
