from .models import TABLE_SPEC, RequestCategory, RequestModel, RequestSentiment, RequestStatus
from app import category_selection, sentiment_analysis
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pathlib import Path
import sqlite3

class RequestAPI(FastAPI):
    """
    Wrapper class for FastAPI with SQLite database integration and helper methods
    for utilizing 3rd-party APIs.
    """

    con: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self, database_location: Path):
        super().__init__()
        self._init_database(database_location)

    def _init_database(self, database_location: Path):
        try:
            self.con = sqlite3.connect(database_location)
            self.con.row_factory = sqlite3.Row
            self.cur = self.con.cursor()
            self.cur.execute(TABLE_SPEC)
        except Exception as e: 
            print("Could not initialize database:\n", e)
            exit(1)

    def close(self):
        self.con.close();
        self.cur.close();

    async def write(self, item: RequestModel) -> sqlite3.Row:
        """Insert new entry into the database. And analyze it using external APIs."""

        if item.id: 
            query = "INSERT INTO requests(id, text, timestamp, status) VALUES (?, ?, ?, ?);"
            self.cur.execute(query, (item.id, item.text, datetime.now(), RequestStatus.open.value))
        else: 
            query = "INSERT INTO requests(text, timestamp, status) VALUES (?, ?, ?);"
            self.cur.execute(query, (item.text, datetime.now(), RequestStatus.open.value))

        if self.cur.lastrowid:
            item_id = self.cur.lastrowid
            self.con.commit()
            await self.analyze(item_id)
        else:
            raise HTTPException(
                status_code=500,
                detail="Internal server error while updating the database.",
                headers={"X-Error": "Database error."},
            )

        data: sqlite3.Row = self.cur.execute("SELECT * FROM requests WHERE id = (?);", (item_id,)).fetchone()
        return data

    async def analyze(self, id: int):
        """Run an entry through external APIs to analyze its sentiment and category."""
        data: sqlite3.Row = self.cur.execute("SELECT * FROM requests WHERE id = (?);", (id,)).fetchone()
        _sentiment = await sentiment_analysis.analyze(data["text"])
        _category = await category_selection.analyze(data["text"])

        try:
            sentiment = RequestSentiment[_sentiment]
        except KeyError:
            sentiment = RequestSentiment.unknown

        try:
            category = RequestCategory[_category]
        except KeyError:
            category = RequestCategory.other

        query = """
            UPDATE requests
            SET sentiment = ?,
                category = ?
            WHERE id = ?
        """

        try:
            self.cur.execute(query, (sentiment.value, category.value, id))
        except Exception as e:
            print(f"Error while updating database after analyzing entry {id}.")
            print(e)
            return

        self.con.commit()

    def read(self, id: int) -> sqlite3.Row:
        """Fetch one entry by its ID."""
        try:
            data = self.cur.execute("SELECT * FROM requests WHERE id = (?);", (id,)).fetchone()
            if not data:
                raise sqlite3.DataError
        except sqlite3.DataError as e:
            raise HTTPException(
                status_code=404,
                detail=f"No entry with the ID {id}",
                headers={"X-Error": "Entry does not exist."},
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500,
                detail="Internal server error while reading the database. See logs for exception info.",
                headers={"X-Error": "Database error."},
            )
        return data

    def read_all(self) -> list[sqlite3.Row]:
        """Fetch all entries from the database."""
        try:
            data: list[sqlite3.Row] = self.cur.execute("SELECT * FROM requests;").fetchall()
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=500,
                detail="Internal server error while reading the database. See logs for exception info.",
                headers={"X-Error": "Database error."},
            )
        return data
