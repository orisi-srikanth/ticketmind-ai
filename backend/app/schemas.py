from pydantic import BaseModel
from typing import List


class TicketRequest(BaseModel):
    ticket_text: str


class TicketResponse(BaseModel):
    category: str
    priority: str
    sentiment: str
    department: str
    urgency: str
    suggested_response: str
    keywords_found: List[str]