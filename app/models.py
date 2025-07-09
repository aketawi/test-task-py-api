from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class RequestStatus(Enum):
    open = "open"
    closed = "closed"

class RequestSentiment(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    unknown = "unknown"

class RequestCategory(Enum):
    technical = "техническая"
    payment = "оплата"
    other = "другое"

class RequestModel(BaseModel):
    """Object model for stored support requests. Optional data will be filled in by the backend."""
    id: int | None = None
    text: str
    timestamp: datetime | None = None
    status: RequestStatus | None = None
    sentiment: RequestSentiment | None = None
    category: RequestCategory | None = None

TABLE_SPEC: str = \
"""
CREATE TABLE IF NOT EXISTS requests(
    id INTEGER PRIMARY KEY,
    text TEXT,
    timestamp TIMESTAMP,
    status TEXT,
    sentiment TEXT,
    category TEXT
);
"""
"""Query to create a SQLite3 table, consistent with RequestModel."""
