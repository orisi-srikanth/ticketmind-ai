DEPARTMENT_MAP = {
    "Payment Issue": "Billing Support",
    "Login Issue": "Account Support",
    "Delivery Issue": "Logistics Support",
    "Refund Issue": "Finance Support",
    "Technical Bug": "Technical Support",
    "Account Issue": "Account Support",
    "Product Issue": "Product Support",
    "General Query": "Customer Support"
}


def route_department(category: str) -> str:
    return DEPARTMENT_MAP.get(category, "Customer Support")