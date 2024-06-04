from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from app.components.LLM.Base import BaseLLMComponent

class OpenAILLMComponent(BaseLLMComponent):
    def __init__(self, openai_api_key):
        super().__init__()
        self.openai_api_key = openai_api_key

    def build(self, temperature=0.7):
        template = """Question: {question}
        Answer: Let's think step by step."""
        self.prompt = PromptTemplate.from_template(template)
        self.llm = OpenAI(openai_api_key=self.openai_api_key, temperature=temperature)

    def run(self, prompt):
        if self.llm is None:
            raise ValueError("LLM is not initialized. Call the build method first.")
        llm_chain = self.prompt | self.llm
        return llm_chain.invoke(prompt)   