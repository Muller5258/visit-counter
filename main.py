import os
import psycopg
from fastapi import FastAPI

app = FastAPI()
DB_URL = os.environ["DATABASE_URL"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def visit():
    with psycopg.connect(DB_URL) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, at TIMESTAMPTZ DEFAULT now())")
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        count = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return {"visits": count}
