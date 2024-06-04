class BaseLLMComponent:
    def __init__(self):
        self.llm = None

    def build(self, **kwargs):
        raise NotImplementedError("You need to implement the build method.")

    def run(self, prompt):
        if self.llm is None:
            raise ValueError("LLM is not initialized. Call the build method first.")
        return self.llm(prompt)