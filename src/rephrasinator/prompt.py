from typing import Optional

from langchain.prompts import PromptTemplate


def get_prompt(
    sentence_to_rephrase: str,
    desired_style: Optional[str],
) -> PromptTemplate:
    return PromptTemplate.from_template(
        _get_prompt_text(sentence_to_rephrase, desired_style),
    )


def _get_prompt_text(sentence_to_rephrase: str, desired_style: Optional[str]) -> str:
    return f"""
            Rephrase the following sentence: {sentence_to_rephrase}.
            Number them from 1 to 10 in style: '1. TEXT'
            Give only the answers, no other text.
            No extra punctuation or information.
            Don't add any extra information.
            Don't add extra newlines.
            """ + (
        f"Give multiple rephrasings in the style of {desired_style}."
        if desired_style is not None
        else ""
    )
