class Persona():

    def __init__(self,nombre, edad):
        self.__nombre= nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad >=0:
            self.__edad=edad 

    def __str__(self):
        return f"Nombre: {self.__nombre} - Edad: {self.__edad}\n"               

    def mayor_de_edad(self):
        if self.__edad >=18:
            return True
        else:
            return False

    def es_mayor_que(self,persona):
        diferencia = self.edad - persona.edad
        return f"La diferencia de edad es de {diferencia} años"            
##PROGRAMA

p=Persona("Pablo",0)
print(p)
p1 =Persona("Cecilia",45)
print(p.es_mayor_que(p1))
print(p.mayor_de_edad())
print(p)
