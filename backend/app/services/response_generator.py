def generate_response(category: str, priority: str, department: str) -> str:
    if priority == "Critical":
        return (
            f"We understand the seriousness of your {category.lower()}. "
            f"Your ticket has been marked as critical and forwarded to {department}. "
            "Our team will prioritize this issue."
        )

    if priority == "High":
        return (
            f"Your {category.lower()} has been registered successfully. "
            f"It has been forwarded to {department} for quick attention."
        )

    if priority == "Medium":
        return (
            f"Thank you for contacting us. Your {category.lower()} has been sent to "
            f"{department}. Our team will review it soon."
        )

    return (
        f"Thank you for reaching out. Your query has been forwarded to "
        f"{department}. We will assist you shortly."
    )