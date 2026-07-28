from sqlalchemy import Column, Integer, String, Float, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    slug = Column(String(50), unique=True, nullable=False)

    movies = relationship("Movie", secondary=movie_genre, back_populates="genres")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    original_title = Column(String(200), nullable=True)
    year = Column(Integer, nullable=False)
    country = Column(String(100), nullable=True)
    duration_min = Column(Integer, nullable=True)
    rating = Column(Float, default=0.0)
    description = Column(Text, nullable=True)
    poster = Column(String(500), nullable=True)
    backdrop = Column(String(500), nullable=True)
    youtube_id = Column(String(50), nullable=True)
    director = Column(String(150), nullable=True)
    cast = Column(String(300), nullable=True)
    is_featured = Column(Integer, default=0)
    views = Column(Integer, default=0)

    genres = relationship("Genre", secondary=movie_genre, back_populates="movies")
