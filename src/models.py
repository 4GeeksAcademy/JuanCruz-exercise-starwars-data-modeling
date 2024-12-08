import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    email = Column(String(50),nullable=False)
   
    

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250),nullable = False)
    age = Column(String(250),nullable = False)
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key= True)
    description = Column(String(250),nullable= False)

    
class Favcharacters(Base):
    __tablename__ = 'Fav_character'
    id = Column(Integer, primary_key= True)
    char_id = Column(Integer, ForeignKey('character.id'),primary_key= True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable = False)       


class Favplanets(Base):
    __tablename__ = 'Fav_planets'
    id = Column(Integer, primary_key= True)
    char_id = Column(Integer, ForeignKey('planets.id'),primary_key= True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable = False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
