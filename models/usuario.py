class Usuario:

    #Connstructor 
    def __init__(self, id, nombre, matricula, carrera, correo):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
    
    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False


def mostrar_info(self):
    return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera}, Correo: {self.correo}"