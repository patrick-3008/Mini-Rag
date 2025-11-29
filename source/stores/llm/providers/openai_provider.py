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
