from database import conexion
from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO: 

    # SELECT * FROM Usuario
    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuario")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = Usuario(id = registro[0],
                            nombre = registro[1], 
                            matricula = registro[2], 
                            carrera = registro[3], 
                            correo = registro[4]
                            )
            usuarios.append(usuario)
            
        cursor.close()
        conexion.close()
        return usuarios
    
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """

            INSERT INTO usuario (nombre, matricula, carrera, correo)
            VALUES (%s, %s, %s, %s)

        """

        cursor.execute(
            sql, (usuario.nombre, usuario.matricula, usuario.carrera, usuario.correo) 
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """

            UPDATE usuario SET nombre = %s, matricula = %s, carrera = %s, correo = %s WHERE id = %s
            
        """        

        cursor.execute(
            sql, (usuario.nombre, usuario.matricula, usuario.carrera, usuario.correo, usuario.id)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,)) 

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]