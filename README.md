# FastAPI Microservices – Layered & Domain-Driven Architecture
This project demonstrates a production-grade FastAPI microservice architecture based on clean layering, domain services, and dependency injection.
It is designed to match real-world backend systems used in enterprise environments.


ARCHITECTURE
Client
  ↓
FastAPI Gateway (HTTP + API)
  ↓
Domain Microservices
   ├── Business Logic
   └── Data / Store


CURRENT IMPLEMENTATION
It exposes the endpoint:
GET /hello

Flow of a request:
HTTP Request
 → Transport Layer (FastAPI Router)
 → API Layer (Orchestration)
 → Hello Domain Service (Business Logic)
 → Hello Repository (Store)
 → Response

Output:
{
  "message": "Hello World"
}

FOLDER STRUCTURE
app/
├── app.py                 # FastAPI bootstrap + dependency injection
├── transport/             # HTTP layer (routes & handlers)
├── api/                   # API orchestration layer
├── services/              # Domain microservices
│   └── hello/
│       ├── service.py     # Business logic
│       └── repo.py        # Data access




