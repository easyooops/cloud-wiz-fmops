class AbstractLLMComponent:
    def __init__(self):
        self.model_instance = None

    def configure(self, **kwargs):
        raise NotImplementedError("The configure method needs to be implemented.")

    def execute(self, input_text):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance(input_text)
