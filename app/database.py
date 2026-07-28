import os
import shutil
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_DB = BASE_DIR / "sql_app.db"
TMP_DB = Path("/tmp/sql_app.db")

# Agar Vercel muhitida bo'lsak, bazani yozish mumkin bo'lgan /tmp papkasiga nusxalaymiz
if ORIGINAL_DB.exists() and not TMP_DB.exists():
    try:
        shutil.copy(ORIGINAL_DB, TMP_DB)
    except Exception as e:
        print(f"Baza nusxalashda xatolik: {e}")

# Vercel'da /tmp ichidagi bazadan, lokalda esa asl bazadan foydalanamiz
if TMP_DB.exists():
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{TMP_DB}"
else:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{ORIGINAL_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()