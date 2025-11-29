from ..llm_interface import LLMInterface
from ..LLMEnums import OpenAIEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):

    def __init__(
            self,
            api_key: str,
            api_url: str = None,
            max_input_char: int=1000,
            max_output_tokens: int=1000,
            temperature: float=0.1
        ):

        self.api_key = api_key
        self.api_url = api_url
        self.max_input_char = max_input_char
        self.max_output_tokens = max_output_tokens
        self.temperature = temperature

        self.generation_model_id = None
        self.embedding_model_id = None
        self.embedding_size = None

        self.client = OpenAI(api_key=self.api_key, api_base=self.api_url)

        self.logger = logging.getLogger(__name__) # takes file name as logger name


    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id # to change while runtime if needed

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size


    def embed_text(self, text: str, document_type: str = None):
        if not self.client:
            self.logger.error("OpenAI client was not set")
            return None

        if not self.embedding_model_id:
            self.logger.error("Embedding model for OpenAI was not set")
            return None
        
        response = self.client.embeddings.create(
            model = self.embedding_model_id,
            input = text,
        )

        if not response or not response.data or len(response.data) == 0 or not response.data[0].embedding:
            self.logger.error("Error while embedding text with OpenAI")
            return None

        return response.data[0].embedding

    def generate_text(
            self,
            prompt: str,
            chat_history: list=[],
            max_output_tokens: int=None,
            temperature: float = None
        ):

        raise NotImplementedError("Method not implemented yet.")
