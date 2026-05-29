NEGATIVE_WORDS = [
    "bad",
    "worst",
    "angry",
    "frustrated",
    "disappointed",
    "not working",
    "failed",
    "problem",
    "issue",
    "complaint",
    "poor",
    "hate",
    "terrible",
    "useless"
]

POSITIVE_WORDS = [
    "good",
    "great",
    "excellent",
    "happy",
    "thanks",
    "thank you",
    "helpful",
    "resolved",
    "satisfied"
]


def detect_sentiment(cleaned_text: str) -> str:
    negative_count = 0
    positive_count = 0

    for word in NEGATIVE_WORDS:
        if word in cleaned_text:
            negative_count += 1

    for word in POSITIVE_WORDS:
        if word in cleaned_text:
            positive_count += 1

    if negative_count > positive_count:
        return "Negative"

    if positive_count > negative_count:
        return "Positive"

    return "Neutral"