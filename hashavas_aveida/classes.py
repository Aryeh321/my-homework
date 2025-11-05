import sqlalchemy
from sqlalchemy import create_engine, Column, DateTime, Integer, String
from hashavas_aveida.database import Base, engine, Session

class Aveidah(Base):
    __tablename__ = 'aveidah'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    color = Column(String(100))
    size = Column(String(100))
    shape = Column(String(100))
    location = Column(String(100))

    def __repr__(self):
        return f"<Aveidah(name='{self.name}', color='{self.color}', size='{self.size}', shape='{self.shape}', location='{self.location}')>"


class AveidahFinder:
    def __init__(self, db_session):
        self.lost_objects = db_session.query(Aveidah).all()

    def siman_checker(self, name, color, size, shape, location):
        found_objects = []
        for obj in self.lost_objects:
            if obj.name == name and obj.color == color and obj.size == size and obj.shape == shape and obj.location == location:
                found_objects.append(obj)
        
        return found_objects
