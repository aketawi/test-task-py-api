
from enum import Enum


class RequestStatus(Enum):
    open = "open"
    closed = "closed"

class RequestSentiment(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"

class RequestCategory(Enum):
    technical = "technical"
    payment = "payment"
    other = "other"

class Request:
    id: int
    text: str
    timetstamp: str
    status: RequestStatus
    sentiment: RequestSentiment
    category: RequestCategory
