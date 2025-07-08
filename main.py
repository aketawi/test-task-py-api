import sqlite3
from fastapi import FastAPI
from common import models


def db_connect() -> sqlite3.Cursor:
    # TODO: check if db exists
    query = """
        CREATE TABLE
        requests(
            id SERIAL PRIMARY KEY,
            text VARCHAR(2048),
            status VARCHAR(128),
            timestamp TIMESTAMP,
            sentiment VARCHAR(128),
            category
        )
        """
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(query)
    return cur

if __name__ == "__main__":
    r = models.Request
    print(r)
    app = FastAPI()
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
