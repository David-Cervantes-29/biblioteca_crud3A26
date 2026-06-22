from multiprocessing import connection

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    #SELECT * from libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT 
            libro.id,
            libro.titulo,
            autor.nombre,
            libro.isbn,
            libro.disponible
            FROM libro
            INNER JOIN autor ON
            libro.autor = autor.id
        """

        cursor.execute(sql)
        registro = cursor.fetchall()

        libros = []
        for registro in registro:
            libro = Libro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                isbn=registro[3],
                disponible=registro[4]
            )
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros
    
    def insertar(sefl, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql ="""
        INSERT INTO libro (titulo, autor, isbn, disponible) 
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (libro.titulo, 
             libro.autor, 
             libro.isbn, 
             libro.disponible)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        UPDATE libro
        SET titulo = %s, autor = %s, isbn = %s, disponible = %s
        WHERE id_libro = %s
        """

        cursor.execute(
            sql,
            (libro.titulo, 
             libro.autor, 
             libro.isbn, 
             libro.disponible,
             libro.id_libro)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, libro_id):
        conexion = conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            " DELETE FROM libro WHERE id = %s",
            (libro_id)
                )
        conexion.commit()
        cursor.close()
        conexion.close()
