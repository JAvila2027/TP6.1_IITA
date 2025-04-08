# cinemar api
## descripcion
cinemar es una api desarrollada con fastapi que permite gestionar un sistema de informacion de un cine la app administra peliculas, funciones, salas, butacas, clientes, entradas y empleados mediante crud.py
## caracteristicas
- gestion de **peliculas**, incluyendo titulo, genero, duracion y clasificacion por edad
- programacion de **funciones** vinculadas a una pelicula, sala y horarios
- administracion de **salas** y sus butacas disponibles
- registro y consulta de **clientes** y las entradas adquiridas
- sistema para la gestion de **empleados**, como cajeros, encargados de sala y administradores
- base de datos sqlite para almacenamiento local
## estructura del programa
- **base_datos.py**: configuracion de la conexion con la base de datos
- **crud.py**: funciones para manejar operaciones crud en la base de datos
- **modelos.py**: definicion de los modelos sqlalchemy
- **schemas.py**: definicion de los esquemas pydantic para validacion de datos
- **main.py**: archivo principal que define los endpoints de la api
- **cinemar.db**: archivo sqlite que almacena los datos de la aplicacion
- **requirements.txt**: lista de dependencias necesarias para ejecutar el programa
## requisitos previos
- python 3.13.0 o superior
- gestor de paquetes pip