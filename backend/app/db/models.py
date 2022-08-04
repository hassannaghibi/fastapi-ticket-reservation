from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    #foreignKey relations
    books = relationship("Book", back_populates="user")
    cinemas = relationship("Cinema", back_populates="user")
    
class Cinema(Base):
    __tablename__ = "cinemas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    user_id = Column(Integer, ForeignKey("users.id"))
    #foreignKey relations
    halls = relationship("Hall", back_populates="cinema")
    user = relationship("User", back_populates="cinemas")
    
class Hall(Base):
    __tablename__ = "halls"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    cinema_id = Column(Integer, ForeignKey("cinemas.id"))
    #foreignKey relations
    cinema = relationship("Cinema", back_populates="halls")
    seats = relationship("Seat", back_populates="hall")
    showings = relationship("Showing", back_populates="hall")

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey relations
    showings = relationship("Showing", back_populates="movie")
    
class Showing(Base):
    __tablename__ = "showings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    start = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    end = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    hall_id = Column(Integer, ForeignKey("halls.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    #foreignKey relations
    hall = relationship("Hall", back_populates="showings")
    movie = relationship("Movie", back_populates="showings")
    books = relationship("Book", back_populates="user")
    
class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    hall_id = Column(Integer, ForeignKey("halls.id"))
    #foreignKey relations
    hall = relationship("Hall", back_populates="seats")
    books = relationship("Book", back_populates="user")
    
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    seat_id = Column(Integer, ForeignKey("seats.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    showing_id = Column(Integer, ForeignKey("showings.id"))
    #foreignKey relations
    seat = relationship("Seat", back_populates="books")
    user = relationship("User", back_populates="books")
    showing = relationship("Showing", back_populates="books")
    