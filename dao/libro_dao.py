#DAO: Data Access Object
# Libro_dao: Objeto a adatosnde la tabla libro

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    #SELECT * from libro
    def obetner_todos(self):
        conexion = Conexion.obtener_conexion
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetcahll()

        libros = []
        for registro in registro:
            libro = Libro(registro.id, registro.titulo, registro.autor, registro.isbn, registro.disponible)
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros