from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    #foreignKey relations
    books = relationship("Book", back_populates="user")
    
class Cinema(Base):
    __tablename__ = "cinema"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    desc = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey relations
    halls = relationship("Hall", back_populates="cinema")
    
class Hall(Base):
    __tablename__ = "hall"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    desc = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey relations
    seats = relationship("Seat", back_populates="hall")
    showings = relationship("Showing", back_populates="hall")

class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    desc = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey relations
    showings = relationship("Showing", back_populates="movie")
    
class Showing(Base):
    __tablename__ = "showing"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    start = Column(DateTime, default=datetime.now, nullable=False)
    end = Column(DateTime, default=datetime.now, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    hall_id = Column(Integer, ForeignKey("hall.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    #foreignKey relations
    hall = relationship("Hall", back_populates="showings")
    movie = relationship("Movie", back_populates="showings")
    books = relationship("Book", back_populates="user")
    
class Seat(Base):
    __tablename__ = "seat"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey relations
    hall_id = Column(Integer, ForeignKey("hall.id"))
    hall = relationship("Hall", back_populates="seats")
    books = relationship("Book", back_populates="user")
    
class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)    
    #foreignKey
    seat_id = Column(Integer, ForeignKey("seat.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    showing_id = Column(Integer, ForeignKey("showing.id"))
    #foreignKey relations
    seat = relationship("Seat", back_populates="books")
    user = relationship("User", back_populates="books")
    showing = relationship("Showing", back_populates="books")
    