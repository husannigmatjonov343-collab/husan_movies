from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pydantic import BaseModel
from typing import List, Optional

from ..database import get_db
from ..models import Movie, Genre

router = APIRouter(prefix="/api", tags=["api"])


class GenreOut(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class MovieOut(BaseModel):
    id: int
    title: str
    year: int
    country: Optional[str] = None
    duration_min: Optional[int] = None
    rating: float
    description: Optional[str] = None
    poster: Optional[str] = None
    backdrop: Optional[str] = None
    youtube_id: Optional[str] = None
    director: Optional[str] = None
    cast: Optional[str] = None
    views: int
    genres: List[GenreOut] = []

    class Config:
        from_attributes = True


@router.get("/movies", response_model=List[MovieOut])
async def api_movies(genre: Optional[str] = None, q: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Movie)
    if genre:
        query = query.join(Movie.genres).filter(Genre.slug == genre)
    if q:
        like = f"%{q}%"
        query = query.filter(or_(Movie.title.ilike(like), Movie.director.ilike(like)))
    return query.all()


@router.get("/movies/{movie_id}", response_model=MovieOut)
async def api_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Kino topilmadi")
    return movie


@router.get("/genres", response_model=List[GenreOut])
async def api_genres(db: Session = Depends(get_db)):
    return db.query(Genre).order_by(Genre.name).all()
