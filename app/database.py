import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Agar loyiha Vercel serverida ishlayotgan bo'lsa, /tmp papkasidan foydalanadi
if os.environ.get("VERCEL"):
    DB_PATH = "/tmp/kinosayt.db"
else:
    DB_PATH = "kinosayt.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()