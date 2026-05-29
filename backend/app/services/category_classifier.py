from typing import Tuple, List


CATEGORY_KEYWORDS = {
    "Payment Issue": [
        "payment", "paid", "money", "deducted", "transaction",
        "upi", "card", "wallet", "charged", "billing"
    ],
    "Login Issue": [
        "login", "password", "otp", "signin", "sign in",
        "account access", "forgot password", "authentication"
    ],
    "Delivery Issue": [
        "delivery", "delivered", "order", "shipment", "courier",
        "late", "tracking", "not received"
    ],
    "Refund Issue": [
        "refund", "return", "cashback", "reversal", "money back"
    ],
    "Technical Bug": [
        "crash", "bug", "error", "app", "website", "server",
        "not working", "loading", "failed", "broken"
    ],
    "Account Issue": [
        "account", "profile", "blocked", "suspended", "delete account",
        "update mobile", "email change"
    ],
    "Product Issue": [
        "product", "damaged", "defective", "wrong item", "quality",
        "missing item"
    ],
    "General Query": [
        "help", "information", "query", "question", "support"
    ],
    "Leave Request": [
    "leave", "sick leave", "casual leave", "vacation",
    "holiday", "absence", "absent", "permission", "time off","leaves"
],
}


def classify_category(cleaned_text: str) -> Tuple[str, List[str]]:
    best_category = "General Query"
    max_matches = 0
    found_keywords = []

    for category, keywords in CATEGORY_KEYWORDS.items():
        matches = []

        for keyword in keywords:
            if keyword in cleaned_text:
                matches.append(keyword)

        if len(matches) > max_matches:
            max_matches = len(matches)
            best_category = category
            found_keywords = matches

    return best_category, found_keywords