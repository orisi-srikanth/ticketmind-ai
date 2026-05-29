from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TicketMind AI backend is running"


def test_health_route():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analyze_ticket():
    payload = {
        "ticket_text": "My payment failed but money was deducted from my account. I need urgent help."
    }

    response = client.post("/analyze-ticket", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Payment Issue"
    assert data["priority"] == "Critical"
    assert data["sentiment"] == "Negative"
    assert data["department"] == "Billing Support"
    assert data["urgency"] == "Urgent"
    assert "payment" in data["keywords_found"]