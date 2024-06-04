from app.components.LLM.Base import BaseLLMComponent
from langchain_community.llms import Bedrock
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

class BedrockLLMComponent(BaseLLMComponent):
    def __init__(self, model_id):
        super().__init__()
        self.model_id = model_id

    def build(self):
        llm = Bedrock(
            credentials_profile_name="credentials-bedrock",
            model_id=self.model_id,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )
        self.conversation = ConversationChain(
            llm=llm, verbose=True, memory=ConversationBufferMemory()
        )

    def run(self, prompt):
        if self.llm is None:
            raise ValueError("LLM is not initialized. Call the build method first.")
        return self.conversation.predict(input=prompt)