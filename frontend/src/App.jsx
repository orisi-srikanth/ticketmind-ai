import { useState } from "react";
import "./App.css";

function App() {
  const [ticketText, setTicketText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  
   const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";


  const sampleTickets = [
    "My payment failed but money was deducted from my account. I need urgent help.",
    "I cannot login to my account even after resetting my password.",
    "The app crashes whenever I click the checkout button.",
    "I want to apply for leave tomorrow.",
    "I want leave and I cannot login to my account.",
  ];

  const wait = (milliseconds) => {
    return new Promise((resolve) => setTimeout(resolve, milliseconds));
  };

  const analyzeTicket = async () => {
    setError("");
    setResult(null);

    if (!ticketText.trim()) {
      setError("Please enter a support ticket.");
      return;
    }

    setLoading(true);

    try {
      console.log("API URL:", `${API_BASE_URL}/analyze-ticket`);
     const apiCall = fetch(`${API_BASE_URL}/analyze-ticket`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ticket_text: ticketText,
        }),
      });

      /*
        This guarantees loading animation stays visible
        for at least 1800ms even if backend replies instantly.
      */
      const [response] = await Promise.all([apiCall, wait(1800)]);

      let data = null;

      try {
        data = await response.json();
      } catch {
        data = null;
      }

      if (!response.ok) {
        setError(data?.detail || "Please enter a valid support issue.");
        return;
      }

      setResult(data);
    } catch {
      setError("Service is currently unavailable. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  const clearTicket = () => {
    setTicketText("");
    setResult(null);
    setError("");
  };

  return (
    <main className="app">
      <section className="hero-section">
        <div className="badge">AI Powered Support Automation</div>

        <h1>
          TicketMind <span>AI</span>
        </h1>

        <p>
          Automatically classify support tickets, detect priority, analyze
          sentiment, route departments, and generate professional responses.
        </p>
      </section>

      <section className="dashboard">
        <div className="panel input-panel">
          <div className="panel-header">
            <div>
              <h2>Support Ticket</h2>
              <p>Paste a customer complaint or choose a sample.</p>
            </div>
          </div>

          <textarea
            value={ticketText}
            onChange={(event) => {
              setTicketText(event.target.value);
              setError("");
            }}
            placeholder="Example: My payment failed but money was deducted from my account. I need urgent help."
          />

          <div className="samples">
            {sampleTickets.map((ticket, index) => (
              <button
                key={index}
                type="button"
                className="sample-btn"
                onClick={() => {
                  setTicketText(ticket);
                  setError("");
                  setResult(null);
                }}
              >
                Sample {index + 1}
              </button>
            ))}
          </div>

          {error && <p className="error">{error}</p>}

          <div className="action-row">
            <button
              type="button"
              className="analyze-btn"
              onClick={analyzeTicket}
              disabled={loading}
            >
              {loading ? "AI is analyzing..." : "Analyze Ticket"}
            </button>

            <button
              type="button"
              className="clear-btn"
              onClick={clearTicket}
              disabled={loading}
            >
              Clear
            </button>
          </div>
        </div>

        <div className="panel result-panel">
          {loading ? (
            <div className="loading-state">
              <div className="scanner">
                <span></span>
              </div>

              <h2>Analyzing ticket...</h2>

              <p>
                TicketMind AI is reading the issue, detecting category, checking
                urgency, analyzing sentiment, and preparing a support response.
              </p>

              <div className="loading-steps">
                <div>
                  <span className="dot"></span>
                  Cleaning ticket text
                </div>

                <div>
                  <span className="dot"></span>
                  Detecting category
                </div>

                <div>
                  <span className="dot"></span>
                  Checking priority
                </div>

                <div>
                  <span className="dot"></span>
                  Generating response
                </div>
              </div>
            </div>
          ) : !result ? (
            <div className="empty-state">
              <div className="empty-icon">⚡</div>

              <h2>Analysis will appear here</h2>

              <p>
                Enter a ticket on the left and TicketMind AI will classify it
                into category, priority, sentiment, department, and urgency.
              </p>

              <div className="feature-list">
                <div>Category Detection</div>
                <div>Priority Scoring</div>
                <div>Sentiment Analysis</div>
                <div>Auto Response</div>
              </div>
            </div>
          ) : (
            <>
              <div className="panel-header">
                <div>
                  <h2>Analysis Result</h2>
                  <p>AI-generated support ticket insights.</p>
                </div>
              </div>

              <div className="result-grid">
                <div className="metric-card">
                  <span>Category</span>
                  <strong>{result.category}</strong>
                </div>

                <div className="metric-card">
                  <span>Priority</span>
                  <strong className={`priority ${result.priority.toLowerCase()}`}>
                    {result.priority}
                  </strong>
                </div>

                <div className="metric-card">
                  <span>Sentiment</span>
                  <strong>{result.sentiment}</strong>
                </div>

                <div className="metric-card">
                  <span>Department</span>
                  <strong>{result.department}</strong>
                </div>

                <div className="metric-card wide">
                  <span>Urgency</span>
                  <strong>{result.urgency}</strong>
                </div>
              </div>

              {result.related_categories?.length > 1 && (
                <div className="keyword-card">
                  <h3>Related Categories</h3>

                  <div className="chips">
                    {result.related_categories.map((category, index) => (
                      <span key={index}>{category}</span>
                    ))}
                  </div>
                </div>
              )}

              <div className="response-card">
                <h3>Suggested Response</h3>
                <p>{result.suggested_response}</p>
              </div>

              <div className="keyword-card">
                <h3>Keywords Found</h3>

                {result.keywords_found.length > 0 ? (
                  <div className="chips">
                    {result.keywords_found.map((keyword, index) => (
                      <span key={index}>{keyword}</span>
                    ))}
                  </div>
                ) : (
                  <p>No specific keywords found.</p>
                )}
              </div>
            </>
          )}
        </div>
      </section>
    </main>
  );
}

export default App;