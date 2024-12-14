from typing import Optional

from langchain.chains import LLMChain

from rephrasinator.model import LLMModel, get_langchain_model
from rephrasinator.prompt import get_prompt


def get_rephrased_sentence(
    sentence_to_rephrase: str,
    desired_style: Optional[str],
    model=LLMModel.PHI314B,
) -> str:
    prompt = get_prompt(sentence_to_rephrase, desired_style)
    chain = LLMChain(
        llm=get_langchain_model(model),
        prompt=prompt,
    )
    response = chain.invoke({input: prompt})
    return response["text"]
