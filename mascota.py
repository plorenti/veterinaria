
class Mascota():

    #Atributo de clase
    id=0

    def __init__(self, nombre):
        self.__nombre=nombre
        self.especie = ""
        self.__edad = 0
        self.__raza = ""
        self.__duenio = ""
        self.__id = Mascota.id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        if edad >=0:
            self.__edad=edad

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza=raza

    @property
    def duenio(self):
        return self.__duenio

    @duenio.setter
    def duenio(self,duenio):
        self.__duenio=duenio

    def __str__(self):
        return f"Nombre: {self.__nombre} - Raza: {self.__raza} - Edad: {self.__edad}\n"


'''
#debug
nombre = input("Ingresar el nombre:")+"Max"
m = Mascota("Max") 
print(m)
m.edad =12
m.raza="Ovejero Alemán"
print(m)
'''
