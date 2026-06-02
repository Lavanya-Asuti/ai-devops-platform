from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import Counter, generate_latest
from app.incident_analyzer import summarize_logs
from prometheus_client import Counter
import logging
import random

logging.basicConfig(
    filename="app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

request_count = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

INCIDENTS = [
    "Application running normally",
    "CPU spike warning",
    "Memory usage increased",
    "Database latency detected",
    "High response time detected",
    "Container restart detected"
]

@app.get("/")
def home():

    request_count.inc()

    event = random.choice(INCIDENTS)

    logging.info(event)

    return {
        "message": "AI DevOps Platform Running",
        "event": event
    }

@app.get("/health")
def health():

    logging.info("Health check successful")

    return {
        "status": "healthy"
    }

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
    

@app.get("/incident-summary")
def incident_summary():

    return {
        "summary": summarize_logs()
    }