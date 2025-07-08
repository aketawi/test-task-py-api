from fastapi import FastAPI
from common import models, database, sentiment_analysis, category_selection, spamcheck
import dotenv

dotenv.load_dotenv()

# sentiment_analysis.analyze()
# spamcheck.analyze()
# category_selection.analyze()

# cur = database.connect()
# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
