import os
import sys
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = sqlalchemy.orm.declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = "menu_item"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


if __name__ == "__main__":
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
