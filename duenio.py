
class Duenio():
    id=0

    def __init__(self,nombre):
        self.__nombre = nombre
        self.telefono = ""
        self.mail=""
        self.__mascotas = []
        

    def AgregarMascota(self,mascota):
        self.__mascotas.append(mascota)

    def __str__(self):
        datos = ""
        datos +=  f"Nombre: {self.__nombre} - ID: {self.id}\n"
        datos += "Listado de mascotas: \n"
        for m in self.__mascotas:
            datos += str(m)
        datos += "\n"

        return datos    

        
