import os
import dotenv
if not dotenv.load_dotenv():
    if not dotenv.load_dotenv(".."):
        print("Could not find .env file. Try sourcing environment variables manually.")
        exit(1)

from app import api_backend, models
from pathlib import Path
from typing import Any

DB_PATH = "data.db"

app = api_backend.RequestAPI(Path(DB_PATH))

@app.post("/api/v1/requests/new")
async def post_request(item: models.RequestModel) -> dict[str, Any]:
    """
    Creates a new database entry from the given POST request, provided it conforms to RequestModel.
    """
    new_request = await app.write(item)
    # TODO: proper response
    return {
        "id": new_request["id"],
        "status": new_request["status"],
        "sentiment": new_request["sentiment"],
        "category": new_request["category"],
    }

@app.get("/api/v1/requests/")
async def get_all_requests():
    """Fetches all requests stored in the database."""
    return app.read_all()

@app.get("/api/v1/requests/{id}")
async def get_request(id: int):
    """Fetches a request from the database by its ID."""
    return app.read(id) 
