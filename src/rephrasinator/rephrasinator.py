from typing import List, Optional

from langchain.chains import LLMChain

from rephrasinator.model import LLMModel, get_langchain_model
from rephrasinator.prompt import get_prompt


def get_rephrased_sentence(
    sentence_to_rephrase: str,
    additional_request: Optional[str] = None,
    model=LLMModel.PHI314B,
) -> List[str]:
    prompt = get_prompt(sentence_to_rephrase, additional_request)
    chain = LLMChain(
        llm=get_langchain_model(model),
        prompt=prompt,
    )
    response = chain.invoke({input: prompt})
    return _filter_response(response["text"])


def _filter_response(response: str) -> List[str]:
    lines = response.split("\n")
    stripped_lines = [line.split(". ", 1)[1].strip() for line in lines if line]
    return [line for line in stripped_lines if line]
