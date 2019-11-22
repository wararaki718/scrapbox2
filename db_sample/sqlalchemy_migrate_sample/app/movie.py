from sqlalchemy import Column, Integer, String

from base import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    genres = Column(String(128))

    def __repr__(self):
        return f'id={self.id}, title={self.title}, genres={self.genres}'
