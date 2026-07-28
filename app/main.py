import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .database import Base, engine, SessionLocal
from .routers import pages, api
from .models import Genre

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KinoSayt",
    description="FastAPI asosida qurilgan katta kino platformasi",
    version="2.0.0",
)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

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
            request, "404.html", {"genres": genres}, status_code=404
        )
    raise exc


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
