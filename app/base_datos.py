from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./cinemar.db"
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
def get_db():
    """
    genera una sesion de base de datos utilizada como una dependencia en 
    las funciones de fastapi
    cierra automaticamente la sesion al finalizar
    db: instancia de la sesion de base de datos
    """
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()