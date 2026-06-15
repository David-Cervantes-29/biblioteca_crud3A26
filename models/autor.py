class Autor:

    #Constructor
    def __init__(self, id_autor, nombre,):
        self.id_autor = id_autor
        self.nombre = nombre

    def mostrar_info(self):
        return f"Autor ID: {self.id_autor}, Nombre: {self.nombre}"