from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_
import os

from ..database import get_db
from ..models import Movie, Genre

router = APIRouter()

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    genres = db.query(Genre).order_by(Genre.name).all()
    featured = db.query(Movie).filter(Movie.is_featured == 1).order_by(Movie.rating.desc()).limit(6).all()
    trending = db.query(Movie).order_by(Movie.views.desc()).limit(10).all()
    newest = db.query(Movie).order_by(Movie.year.desc()).limit(10).all()
    top_rated = db.query(Movie).order_by(Movie.rating.desc()).limit(10).all()
    total_movies = db.query(Movie).count()

    return templates.TemplateResponse(
        request, "index.html",
        {
            "genres": genres,
            "featured": featured,
            "trending": trending,
            "newest": newest,
            "top_rated": top_rated,
            "total_movies": total_movies,
        },
    )


@router.get("/movie/{movie_id}", response_class=HTMLResponse)
async def watch_movie(request: Request, movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Kino topilmadi")

    movie.views = (movie.views or 0) + 1
    db.commit()

    genre_ids = [g.id for g in movie.genres]
    related = (
        db.query(Movie)
        .join(Movie.genres)
        .filter(Genre.id.in_(genre_ids), Movie.id != movie.id)
        .distinct()
        .limit(8)
        .all()
    )
    genres = db.query(Genre).order_by(Genre.name).all()

    return templates.TemplateResponse(
        request, "movie.html",
        {"movie": movie, "related": related, "genres": genres},
    )


@router.get("/genre/{slug}", response_class=HTMLResponse)
async def genre_page(request: Request, slug: str, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.slug == slug).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Janr topilmadi")

    genres = db.query(Genre).order_by(Genre.name).all()
    movies = genre.movies

    return templates.TemplateResponse(
        request, "genre.html",
        {"genre": genre, "movies": movies, "genres": genres},
    )


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, q: str = "", db: Session = Depends(get_db)):
    genres = db.query(Genre).order_by(Genre.name).all()
    results = []
    if q.strip():
        like = f"%{q.strip()}%"
        results = (
            db.query(Movie)
            .filter(or_(Movie.title.ilike(like), Movie.director.ilike(like), Movie.cast.ilike(like)))
            .all()
        )

    return templates.TemplateResponse(
        request, "search.html",
        {"query": q, "results": results, "genres": genres},
    )
