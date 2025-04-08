from sqlalchemy.orm import Session
from app.modelos import Pelicula, Funcion, Sala, Butaca, Cliente, Entrada, Empleado
from app.schemas import PeliculaCreate, FuncionCreate, SalaCreate, ButacaCreate, ClienteCreate, EntradaCreate, EmpleadoCreate

def create_pelicula(db: Session,pelicula: PeliculaCreate):
    """
    se crea una nueva pelicula
    db (Session) = sesion de la base de datos
    pelicula (PeliculaCreate) = una pelicula a crear
    Pelicula = una pelicula recien creada
    """
    nueva_pelicula=Pelicula(**pelicula.dict())
    db.add(nueva_pelicula)
    db.commit()
    db.refresh(nueva_pelicula)
    return nueva_pelicula
def get_peliculas(db: Session):
    """
    tiene todas las peliculas de la base de datos
    db (Session) = sesion de la base de datos
    List[Pelicula] = una lista de todas las peliculas registradas
    """
    return db.query(Pelicula).all()
def create_funcion(db: Session,funcion: FuncionCreate):
    """
    una nueva funcion en la base de datos
    db (Session) = desion de la base de datos
    funcion (FuncionCreate) = una funcion para crear
    Funcion = la función recien creada
    """
    nueva_funcion=Funcion(**funcion.dict())
    db.add(nueva_funcion)
    db.commit()
    db.refresh(nueva_funcion)
    return nueva_funcion
def get_funciones(db: Session):
    """
    todas las funciones de la base de datos
    db (Session) = sesion de la base de datos
    List [Funcion] = lista de todas las funciones registradas
    """
    return db.query(Funcion).all()
def create_sala(db: Session,sala: SalaCreate):
    """
    nueva sala en la base de datos
    db (Session) = sesion de la base de datos
    sala (SalaCreate) = sala a crear
    Sala = una sala recién creada
    """
    nueva_sala=Sala(**sala.dict())
    db.add(nueva_sala)
    db.commit()
    db.refresh(nueva_sala)
    return nueva_sala
def get_salas(db: Session):
    """
    con todas las salas de la base de datos
    db (Session) = sesion de la base de datos
    List[Sala] = lista de todas las salas registradas
    """
    return db.query(Sala).all()
def create_butaca(db: Session,butaca: ButacaCreate):
    """
    se crea una nueva butaca en la base de datos
    db (Session): sesion de la base de datos
    butaca (ButacaCreate) = la butaca para crearla
    Butaca = una butaca recien creada
    """
    nueva_butaca=Butaca(**butaca.dict())
    db.add(nueva_butaca)
    db.commit()
    db.refresh(nueva_butaca)
    return nueva_butaca
def get_butacas(db: Session):
    """
    todas las butaca de la base de datos
    db (Session) = sesion de la base de datos
    List[Butaca] = una lista de todas las butacas registradas
    """
    return db.query(Butaca).all()
def create_cliente(db: Session,cliente: ClienteCreate):
    """
    es un nuevo cliente en la base de datos
    db (Session) = sesion de la base de datos
    cliente (ClienteCreate) = un cliente a crear
    Cliente = el cliente creado
    """
    nuevo_cliente=Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente
def get_clientes(db: Session):
    """
    es a todos los clientes de la base de datos
    db (Session) = sesion de la base de datos
    List[Cliente] = lista de todos los clientes registrados
    """
    return db.query(Cliente).all()
def create_entrada(db: Session,entrada: EntradaCreate):
    """
    una nueva entrada en la base de datos
    db (Session) = sesion de la base de datos
    entrada (EntradaCreate) = una entrada a crear
    Entrada = una entrada recien creada
    """
    nueva_entrada=Entrada(**entrada.dict())
    db.add(nueva_entrada)
    db.commit()
    db.refresh(nueva_entrada)
    return nueva_entrada
def get_entradas(db: Session):
    """
    son todas las entradas de la base de datos
    db (Session) = sesion de la base de datos
    List[Entrada] = una lista de todas las entradas registradas
    """
    return db.query(Entrada).all()
def create_empleado(db: Session,empleado: EmpleadoCreate):
    """
    crear a nuevo empleado en la base de datos
    db (Session) = sesion de la base de datos
    empleado (EmpleadoCreate) = un empleado para crear
    Empleado = empleado creado
    """
    nuevo_empleado=Empleado(**empleado.dict())
    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)
    return nuevo_empleado
def get_empleados(db: Session):
    """
    todos los empleados de la base de datos
    db (Session) = sesion de la base de datos
    List[Empleado] = la lista de todos los empleados
    """
    return db.query(Empleado).all()