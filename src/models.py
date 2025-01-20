import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

Base = declarative_base()

# Modelo de Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    fecha_suscripcion = Column(DateTime, default=datetime.timezone.utc)
    
    favoritos = relationship("Favorito", back_populates="usuario")

# Modelo de Planeta
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    clima = Column(String, nullable=True)
    terreno = Column(String, nullable=True)
    poblacion = Column(String, nullable=True)
    
    favoritos = relationship("Favorito", back_populates="planeta")

# Modelo de Personaje
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    altura = Column(String, nullable=True)
    peso = Column(String, nullable=True)
    genero = Column(String, nullable=True)
    especie = Column(String, nullable=True)
    
    favoritos = relationship("Favorito", back_populates="personaje")

# Modelo de Favorito
class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    
    usuario = relationship("Usuario", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
