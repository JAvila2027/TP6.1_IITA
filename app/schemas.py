from pydantic import BaseModel
from typing import Optional

class PeliculaBase(BaseModel):
    """
    datos de una pelicula en el sistema
    titulo = titulo de una pelicula
    genero = genero de una pelicula como accion, comedia o otros
    duracion = duracion de una pelicula en minutos
    """
    titulo: str
    genero: str
    duracion: int
class PeliculaCreate(PeliculaBase):
    """
    es para crear una nueva pelicula
    se hereda los atributos de PeliculaBase
    """
    pass
class Pelicula(PeliculaBase):
    """
    una pelicula con los datos leidos desde la base de datos
    id = un indentificador de una pelicula
    """
    id: int
    class Config:
        orm_mode=True
class FuncionBase(BaseModel):
    """
    son datos de una funcion en el cine
    pelicula_id = un identificador de una pelicula proyectada
    sala_id = un identificador de una sala en donde se proyecta la pelicula
    horario = la fecha y hora de la funcion
    """
    pelicula_id: int
    sala_id: int
    horario: str
class FuncionCreate(FuncionBase):
    """
    sirve para crear un funcion
    es heredada de los atributos FuncionBase
    """
    pass
class Funcion(FuncionBase):
    """
    datos leidos desde la base de datos
    id = un indentificador unico de una funcion
    """
    id: int
    class Config:
        orm_mode=True
class SalaBase(BaseModel):
    """
    datos basicos de una sala del cine
    numero = un numero unico que identifica una sala
    capacidad_maxima = capacidad maxima de una sala
    """
    numero: int
    capacidad_maxima: int
class SalaCreate(SalaBase):
    """
    es para crear una nueva sala
    y se hereda los atributos de SalaBase
    """
    pass
class Sala(SalaBase):
    """
    una sala con datos leidos desde la base de datos
    id = un indentificador unico de una sala
    """
    id: int
    class Config:
        orm_mode=True
class ButacaBase(BaseModel):
    """
    los datos de una butaca en una sala
    sala_id = un indentificador de la sala a la que pertenece a la butaca
    fila = una fila en donde se encuentra la butaca
    columna = numero de columna de la butaca en la fila
    estado = el estado de la butaca de si esta ocupada o si esta libre
    """
    sala_id: int
    fila: str
    columna: int
    estado: bool
class ButacaCreate(ButacaBase):
    """
    es para crear una nueva butaca
    se hereda los atributos de ButacaBase
    """
    pass
class Butaca(ButacaBase):
    """
    una butaca con datos leidos desde la base de datos
    id = un indentificador unico de la butaca
    """
    id: int
    class Config:
        orm_mode=True
class ClienteBase(BaseModel):
    """
    son datos de un cliente del cine
    nombre = el nombre completo del cliente
    correo = correo electronico unico del cliente
    telefono = el telefono del cliente
    """
    nombre: str
    correo: str
    telefono: str
class ClienteCreate(ClienteBase):
    """
    crea un nuevo cliente
    se hereda los atributos de la ClienteBase
    """
    pass
class Cliente(ClienteBase):
    """
    un cliente con datos leidos desde la base de datos
    id = un indentificador unico del cliente
    """
    id: int
    class Config:
        orm_mode=True
class EntradaBase(BaseModel):
    """
    datos de una entrada que ya fue comprada
    cliente_id = un indentificador de un cliente que compro la entrada
    funcion_id = un indentificador de una funcion asociada a la entrada
    butaca_id = un indentificador de una butaca que fue asignada
    metodo_compra = el metodo de compra de una entrada
    """
    cliente_id: int
    funcion_id: int
    butaca_id: int
    metodo_compra: str
class EntradaCreate(EntradaBase):
    """
    es para crear una nueva entrada
    se hereda los atributos de EntradaBase
    """
    pass
class Entrada(EntradaBase):
    """
    es una entrada con datos leidos desde la base de datos
    id = un indentificador unico de la entrada
    """
    id: int
    class Config:
        orm_mode=True
class EmpleadoBase(BaseModel):
    """
    un empleado del cine
    nombre = nombre del empleado
    correo = correo electronico del empleado
    rol = rol del empleado
    """
    nombre: str
    correo: str
    rol: str
class EmpleadoCreate(EmpleadoBase):
    """
    se crea un nuevo empleado
    se hereda los atributos de EmpleadoBase
    """
    pass
class Empleado(EmpleadoBase):
    """
    es un empleado con datos leidos desde la base de datos
    id = un indentificador unico del empleado
    """
    id: int
    class Config:
        orm_mode=True