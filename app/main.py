from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app.base_datos import get_db
from app.schemas import (
    PeliculaCreate, Pelicula,FuncionCreate,Funcion,
    SalaCreate,Sala,ButacaCreate,Butaca,
    ClienteCreate,Cliente,EntradaCreate,Entrada,
    EmpleadoCreate,Empleado
)
from app.crud import (
    create_pelicula,get_peliculas,create_funcion,get_funciones,
    create_sala,get_salas,create_butaca,get_butacas,
    create_cliente,get_clientes,create_entrada,get_entradas,
    create_empleado,get_empleados
)
app=FastAPI()
@app.post("/peliculas/",response_model=Pelicula)
def crear_pelicula(pelicula: PeliculaCreate,db: Session=Depends(get_db)):
    """
    se crea una nueva película
    pelicula (PeliculaCreate) = datos de la película para crear
    db (Session) = sesion de la base de datos
    Pelicula = una pelicula recien creada
    """
    return create_pelicula(db,pelicula)
@app.get("/peliculas/", response_model=List[Pelicula])
def leer_peliculas(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    una lista de todas las peliculas registradas
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Pelicula] = lista de peliculas registradas
    """
    return get_peliculas(db,skip=skip,limit=limit)
@app.post("/funciones/",response_model=Funcion)
def crear_funcion(funcion: FuncionCreate,db: Session=Depends(get_db)):
    """
    crea una nueva funcion
    funcion (funcioncreate) = datos de la funcion a crear
    db (session) = sesion de la base de datos
    funcion = funcion recien creada
    """
    return create_funcion(db,funcion)
@app.get("/funciones/",response_model=List[Funcion])
def leer_funciones(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    lista de todas las funciones registradas
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Funcion] = lista de funciones registradas

    """
    return get_funciones(db,skip=skip,limit=limit)
@app.post("/salas/",response_model=Sala)
def crear_sala(sala: SalaCreate,db: Session=Depends(get_db)):
    """
    crea una nueva sala
    sala (salacreate) = datos de la sala a crear
    db (Session) = sesion de la base de datos
    sala = sala recien creada
    """
    return create_sala(db,sala)
@app.get("/salas/",response_model=List[Sala])
def leer_salas(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    lista de todas las salas registradas
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Sala] = lista de salas registradas
    """
    return get_salas(db,skip=skip,limit=limit)
@app.post("/butacas/",response_model=Butaca)
def crear_butaca(butaca: ButacaCreate,db: Session=Depends(get_db)):
    """
    crea una nueva butaca
    butaca (butacacreate) = datos de la butaca a crear
    db (Session) = sesion de la base de datos
    Butaca: butaca recien creada
    """
    return create_butaca(db,butaca)
@app.get("/butacas/",response_model=List[Butaca])
def leer_butacas(skip: int = 0,limit: int=10, db: Session=Depends(get_db)):
    """
    lista de todas las butacas registradas
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Butaca] = lista de butacas registradas
    """
    return get_butacas(db,skip=skip,limit=limit)
@app.post("/clientes/",response_model=Cliente)
def crear_cliente(cliente: ClienteCreate,db: Session=Depends(get_db)):
    """
    crea un nuevo cliente
    cliente (ClienteCreate) = los datos del cliente a crear.
    db (Session) = sesion de la base de datos
    Cliente = cliente creado
    """
    return create_cliente(db,cliente)
@app.get("/clientes/",response_model=List[Cliente])
def leer_clientes(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    una lista de todos los clientes
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Cliente] = lista de clientes registrados
    """
    return get_clientes(db,skip=skip,limit=limit)
@app.post("/entradas/",response_model=Entrada)
def crear_entrada(entrada:EntradaCreate,db:Session=Depends(get_db)):
    """
    una nueva entrada en el sistema
    entrada (EntradaCreate) = los datos de la entrada a crear
    db (Session) = sesion de la base de datos
    Entrada = entrada creada
    """
    return create_entrada(db,entrada)
@app.get("/entradas/", response_model=List[Entrada])
def leer_entradas(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    una lista de todas las entradas
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Entrada] = lista de entradas registradas
    """
    return get_entradas(db,skip=skip,limit=limit)
@app.post("/empleados/",response_model=Empleado)
def crear_empleado(empleado: EmpleadoCreate,db: Session=Depends(get_db)):
    """
    crea un nuevo empleado
    empleado (EmpleadoCreate) = los datos del empleado a crear
    db (Session) = sesion de la base de datos
    Empleado = empleado recien creado
    """
    return create_empleado(db,empleado)
@app.get("/empleados/",response_model=List[Empleado])
def leer_empleados(skip: int=0,limit: int=10,db: Session=Depends(get_db)):
    """
    una lista de todos los empleados
    skip (int) = numero de registros a omitir
    limit (int) = numero maximo de registros a devolver
    db (Session) = sesion de la base de datos
    List[Empleado] = lista de empleados registrados
    """
    return get_empleados(db,skip=skip,limit=limit)