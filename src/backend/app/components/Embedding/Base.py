from langchain_openai import OpenAIEmbeddings

class AbstractEmbeddingComponent:
    def __init__(self):
        self.model_instance = None

    def configure(self, **kwargs):
        raise NotImplementedError("The configure method needs to be implemented")

    def execute(self, input_text):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance(input_text)

    def execute_embed_query(self, input_text):
        raise NotImplementedError("The execute_embed_query method needs to be implemented")

    def execute_embed_documents(self, documents: list):
        raise NotImplementedError("The execute_embed_documents method needs to be implemented")