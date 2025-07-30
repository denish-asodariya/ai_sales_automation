import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db/automation.db")
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    with engine.connect() as conn:
        with open("db/schema.sql") as f:
            conn.execute(text(f.read()))
    print("Database initialized!")

if __name__ == "__main__":
    init_db()
