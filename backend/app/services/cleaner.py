import re


def clean_text(text: str) -> str:
    """
    Cleans ticket text:
    1. Converts to lowercase
    2. Removes symbols
    3. Removes extra spaces
    """

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text