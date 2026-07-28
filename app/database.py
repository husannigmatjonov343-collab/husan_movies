import os
import shutil
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Loyihaning ildiz (root) papkasini aniqlash
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent if CURRENT_DIR.name == "app" else CURRENT_DIR

# 2. Baza fayli nomi
# (Agar faylingiz nomi 'sql_app.db' bo'lsa, pastdagi 'kinosayt.db'ni 'sql_app.db'ga o'zgartiring)
DB_NAME = "kinosayt.db"

ORIGINAL_DB_PATH = BASE_DIR / DB_NAME
TMP_DB_PATH = Path(f"/tmp/{DB_NAME}")

# 3. Vercel muhitida faylni yozish va o'qish mumkin bo'lgan /tmp papkasiga nusxalash
if ORIGINAL_DB_PATH.exists() and not TMP_DB_PATH.exists():
    try:
        shutil.copyfile(ORIGINAL_DB_PATH, TMP_DB_PATH)
    except Exception as e:
        print(f"DB faylini /tmp ga nusxalashda xatolik: {e}")

# 4. Qaysi yo'ldan foydalanishni tanlash
if TMP_DB_PATH.exists():
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{TMP_DB_PATH}"
else:
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{ORIGINAL_DB_PATH}"

# 5. SQLAlchemy Engine va Session yaratish
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 6. Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()