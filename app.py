from dao import libro_dao
from dao.libro_dao import LibroDAO
from models import autor, libro
from models.libro import Libro


def ver_libros():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print("No hay Libros Registrados")
        else:
            for libro in libros:
                print("-----------------------------")
                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo}, "
                    f"Autor: {libro.autor}, ISBN: {libro.isbn}, "
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("------------------------------")
        print("\n Conexion Exitosa a la Base de Datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    titulo = input("Escribe el titulo del libro: ")
    autor = int(input("Escribe el nombre del autor: "))
    isbn = input("Escriba el isbn del nuevo libro: ")
    disponible = True

    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al insertar un libro nuevo")
        print(e)

def actualizar_libro():
    print("Seleciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id de libro a actualizar: "))
        titulo = input("Escribe el nuevo titulo: ")
        autor = input("Escribe el nuevo autor: ")
        isbn = input("Escribe el nuevo ISBN: ")
        disponible = bool(input("Escribe el nuevo valor de disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado existosament")
        
    except Exception as e:
        print("Error al actualizar un libro")
        print(e)

def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menu de opciones")
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro disponible")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
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

if __name__ == "__main__":
    main() 