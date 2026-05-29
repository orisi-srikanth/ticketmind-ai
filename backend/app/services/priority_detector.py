CRITICAL_WORDS = [
    "urgent",
    "immediately",
    "emergency",
    "critical",
    "money deducted",
    "payment failed",
    "account blocked",
    "cannot login",
    "security",
    "fraud"
]

HIGH_WORDS = [
    "not working",
    "failed",
    "delay",
    "angry",
    "issue",
    "problem",
    "complaint",
    "not received",
    "crash"
]

MEDIUM_WORDS = [
    "slow",
    "confused",
    "need help",
    "please check",
    "update",
    "change"
]


def detect_priority(cleaned_text: str) -> str:
    for word in CRITICAL_WORDS:
        if word in cleaned_text:
            return "Critical"

    for word in HIGH_WORDS:
        if word in cleaned_text:
            return "High"

    for word in MEDIUM_WORDS:
        if word in cleaned_text:
            return "Medium"

    return "Low"


def detect_urgency(priority: str) -> str:
    if priority == "Critical":
        return "Urgent"

    if priority == "High":
        return "Needs Quick Attention"

    if priority == "Medium":
        return "Normal"

    return "Low Urgency"