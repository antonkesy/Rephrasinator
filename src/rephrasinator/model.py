from enum import Enum

from langchain_community.llms import Ollama
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI


# https://platform.openai.com/docs/models/model-endpoint-compatibility
# https://github.com/ollama/ollama?tab=readme-ov-file#model-library
# https://ollama.com/library
class LLMModel(str, Enum):
    GPTTurbo = "gpt-3.5-turbo"
    LLAMA3 = "llama3"
    GPT4 = "gpt-4"
    PHI314B = "phi3:14b"


def get_model(model: LLMModel) -> BaseChatModel:
    match model:
        case LLMModel.GPTTurbo | LLMModel.GPT4:
            ai_model = ChatOpenAI(temperature=0, model=model.value)
        case LLMModel.PHI314B | LLMModel.LLAMA3:
            ai_model = Ollama(model=model.value)
    return ai_model
