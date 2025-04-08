from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()
class Pelicula(Base):
    """
    se basa en las peliculas que hay en el cine con su informacion
    id = un identificador unico de una pelicula
    titulo = el nombre de una pelicula
    genero = genero de una pelicula
    duracion = duracion en minutos
    funciones = la relacion con la funciones y en como se proyecta la pelicula
    """
    __tablename__="peliculas"
    id=Column(Integer,primary_key=True,index=True)
    titulo=Column(String,index=True)
    genero=Column(String)
    duracion=Column(Integer)
    funciones=relationship("Funcion",back_populates="pelicula")
class Funcion(Base):
    """
    una funcion en donde se proyecta una pelicula
    id = un identificador unico de una pelicula
    pelicula_id = un identificador unico de una pelicula
    sala_id = un identificador unico de una sala
    horario = la fecha y la hora de una funcion
    pelicula = relacion con una pelicula proyectada
    sala = relacion de una sala proyectada
    """
    __tablename__="funciones"
    id=Column(Integer,primary_key=True,index=True)
    pelicula_id=Column(Integer,ForeignKey("peliculas.id"),nullable=False)
    sala_id=Column(Integer,ForeignKey("salas.id"),nullable=False)
    horario=Column(String,nullable=False)
    pelicula=relationship("Pelicula",back_populates="funciones")
    sala=relationship("Sala",back_populates="funciones")
class Sala(Base):
    """
    id = un identificador unico de una sala
    numero = numero de una sala
    capacidad_maxima = la capacidad maxima de una sala
    funciones = relacion de una sala proyectada
    """
    __tablename__="salas"
    id=Column(Integer,primary_key=True,index=True)
    numero=Column(Integer,unique=True,index=True)
    capacidad_maxima=Column(Integer)
    funciones=relationship("Funcion",back_populates="sala")
class Butaca(Base):
    """
    id = un identificador unico de una butaca
    sala_id = identificador unico de una sala
    fila = en donde se encuentra la butaca
    columna = columna en donde se encuentra la butaca
    estado = estado de la butaca ocupada o libre
    sala = relacion con la sala a que pertenece
    """
    __tablename__="butacas"
    id=Column(Integer,primary_key=True,index=True)
    sala_id=Column(Integer,ForeignKey("salas.id"))
    fila=Column(String)
    columna=Column(Integer)
    estado=Column(Boolean,default=False)
    sala=relationship("Sala")
class Cliente(Base):
    """
    se basa a un cliente que va al cine
    id = identificador unico del cliente
    nombre = nombre del cliente
    correo = correo electronico del cliente
    telefono = telefono del cliente
    entradas = relacion con las entradas compradas por los clientes
    """
    __tablename__="clientes"
    id=Column(Integer,primary_key=True,index=True)
    nombre=Column(String,index=True)
    correo=Column(String,unique=True,index=True)
    telefono=Column(String)
    entradas=relationship("Entrada",back_populates="cliente")
class Entrada(Base):
    """
    entradas compradas para una funcion
    id = identificador unico de una entrada
    cliente_id = un identificador del cliente que compro la entrada
    funcion_id = un identificador de la funcion
    butaca_id = un identificador de una butaca asignada
    metodo_compra = metodo de compra
    cliente = el cliente que hizo la compra
    funcion = la funcion de la entrada
    butaca = la butaca que fue asignada
    """
    __tablename__="entradas"
    id=Column(Integer,primary_key=True,index=True)
    cliente_id=Column(Integer,ForeignKey("clientes.id"))
    funcion_id=Column(Integer,ForeignKey("funciones.id"))
    butaca_id=Column(Integer,ForeignKey("butacas.id"))
    metodo_compra=Column(String)
    cliente=relationship("Cliente",back_populates="entradas")
    funcion=relationship("Funcion")
    butaca=relationship("Butaca")
class Empleado(Base):
    """
    representa a un empleado del cine
    id = un identificador unico del empleado
    nombre = nombre del empleado
    correo = correo electrónico del empleado
    rol = el rol del empleado como cajero, administrador, otros
    """
    __tablename__="empleados"
    id=Column(Integer,primary_key=True,index=True)
    nombre=Column(String,index=True)
    correo=Column(String,unique=True,index=True)
    rol=Column(String)