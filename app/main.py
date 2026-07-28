from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from .database import Base, engine, SessionLocal
from .routers import pages, api
from .models import Genre

# Loyihaning asosiy papka yo'lini aniqlash (pathlib orqali zamonaviy usul)
BASE_DIR = Path(__file__).resolve().parent


# Database jadvallarini ilova ishga tushganda yaratish (Lifespan usuli)
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="KinoSayt",
    description="FastAPI asosida qurilgan katta kino platformasi",
    version="2.0.0",
    lifespan=lifespan,
)

# Statik fayllar va shablonlarni (templates) ulash
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Routerni ilovaga qo'shish
app.include_router(pages.router)
app.include_router(api.router)


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        db = SessionLocal()
        try:
            genres = db.query(Genre).order_by(Genre.name).all()
        finally:
            db.close()

        return templates.TemplateResponse(
            name="404.html",
            context={"request": request, "genres": genres},
            status_code=404,
        )
    raise exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        genres = []
        try:
            db = SessionLocal()
            genres = db.query(Genre).order_by(Genre.name).all()
            db.close()
        except Exception as e:
            print(f"404 DB Error: {e}")

        return templates.TemplateResponse(
            name="404.html",
            context={"request": request, "genres": genres},
            status_code=404,
        )
    raise exc