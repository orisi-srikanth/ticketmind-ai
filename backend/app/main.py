from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import TicketRequest, TicketResponse
from app.services.cleaner import clean_text
from app.services.category_classifier import classify_category
from app.services.priority_detector import detect_priority, detect_urgency
from app.services.sentiment_detector import detect_sentiment
from app.services.router import route_department
from app.services.response_generator import generate_response


app = FastAPI(
    title="TicketMind AI",
    description="NLP-based support ticket classification and priority detection system",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "TicketMind AI backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/analyze-ticket", response_model=TicketResponse)
def analyze_ticket(request: TicketRequest):
    cleaned_text = clean_text(request.ticket_text)

    category, keywords_found = classify_category(cleaned_text)
    priority = detect_priority(cleaned_text)
    urgency = detect_urgency(priority)
    sentiment = detect_sentiment(cleaned_text)
    department = route_department(category)
    suggested_response = generate_response(category, priority, department)

    return TicketResponse(
        category=category,
        priority=priority,
        sentiment=sentiment,
        department=department,
        urgency=urgency,
        suggested_response=suggested_response,
        keywords_found=keywords_found
    )