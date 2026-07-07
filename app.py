from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario 

def ver_libros():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos()

        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print("================================================================================")
                print(f"id: {libro.id}, {libro.titulo}, {libro.autor}, {libro.isbn}, {libro.disponible}")
                print("================================================================================")
        print(f"\n Conexion exitosa con la base de datos")

    except Exception as e:
        print("Error")            
        print(e)

def insertar_libro():
    titulo = input("Escribe el titulo del nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn del nuevo libro: ")
    disponible = True

    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1 

        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con exito")

    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)


def actualizar_libro():
    try:
        libro_dao = LibroDAO()  

        print("Lista de libros disponibles")  
        ver_libros() 

        id = int(input("Seleccione el id de el libro a actualizar: "))   
        titulo = input("Escribe el titulo: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el isbn: ")
        disponible = bool(input("Escribe si esta disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)

        libro_dao.actualizar(libro)
        print(f"El libro {id} fue actualizado con exito")

    except Exception as e:
        print("Error al actualizar el libro")    
        print(e)


def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        
        print("Lista de libros disponibles")
        ver_libros()

        id = int(input("Escriba el id de el libro a eliminar: "))
        libro_dao.eliminar(id)

        print(f"El libro {id} ha sido eliminado con exito")

    except Exception as e:
        print(f"Error al eliminar el libro {id}")   
        print(e)         

def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        usuarios = usuario_dao.obtener_todo()

        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print("===============================================================================================================")
                print(f"id: {usuario.id}, {usuario.nombre}, {usuario.matricula}, {usuario.carrera}, {usuario.correo}")
                print("===============================================================================================================")

            print(f"\nConexion exitosa con la base de datos")

    except Exception as e:
        print("Error")            
        print(e)

def insertar_usuario():
    nombre = input("Escribe un nuevo usuario: ")
    matricula = input("Escribe la matricula: ")
    carrera = int(input("Escribe la carrera: "))
    correo = input("Escribe el correo: ")


    try:
        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1 

        nuevo_usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.insertar(nuevo_usuario)
        print("Insercion realizada con exito")

    except Exception as e:
        print("Error al insertar un nuevo usuario")
        print(e)

def actualizar_usuario():
    try:
        usuario_dao = UsuarioDAO()  

        print("Lista de usuarios activos")  
        ver_usuarios() 

        id = int(input("Seleccione el id de el usuario a actualizar: "))   
        nombre = input("Escribe el nombre: ")
        matricula = input("Escribe el id de la matricula: ")
        carrera = input("Escribe la carrera: ")
        correo = input("Escribe el correo: ")

        usuario = Usuario(id, nombre, matricula, carrera, correo,)

        usuario_dao.actualizar(usuario)
        print(f"El usuario {id} fue actualizado con exito")

    except Exception as e:
        print("Error al actualizar el usuario")    
        print(e)
   

def eliminar_usuario():
   
    try:
        usuario_dao = UsuarioDAO()
        
        print("Lista de usuarios activos")
        ver_usuarios()

        id = int(input("Escriba el id de el usuario a eliminar: "))
        usuario_dao.eliminar(id)

        print(f"El usuario {id} ha sido eliminado con exito")

    except Exception as e:
        print(f"Error al eliminar el usuario {id}")   
        print(e)

def menu_libros():
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")
    opcion = int(input("Selecciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()         

def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario existente")
    opcion = int(input("Selecciona un opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuario()    
        case 3:
            actualizar_usuario()   
        case 4:
            eliminar_usuario()

def main():
    print("=== BIBLIOTECA UNIVERSITARIA === ") 
    print("Menu de opciones: ")
    print("1. Libros")
    print("2. Usuarios")
    opcion = int(input("Escribe tu opcion: "))
    match opcion:
        case 1: menu_libros()
        case 2: menu_usuarios() 

    print("Saliendo del sistema de Biblioteca universitaria ... ")    
            
if __name__ == "__main__":
    main()