import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Loyihaning asosiy papkasi
BASE_DIR = Path(__file__).resolve().parent.parent

# Vercel Environment Variables bo'limidan DATABASE_URL ni olish
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # Ba'zi bulutli servislar (masalan, Supabase/Neon) "postgres://" berishi mumkin.
    # SQLAlchemy esa modern "postgresql://" formatini talab qiladi.
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    # Bulutli PostgreSQL bazasi uchun engine
    engine = create_engine(DATABASE_URL)
else:
    # Lokal kompyuterda ishlatish uchun SQLite bazasi
    DB_PATH = BASE_DIR / "sql_app.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"
    
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