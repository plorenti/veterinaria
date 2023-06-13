from duenio import Duenio
from mascota import Mascota

class Veterinaria():
    def __init__(self,nombre):
        self.nombre = nombre
        self.__mascotas = []


    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def __str__(self):
        datos =""
        datos += f"Sistema {self.nombre}\n"
        datos += "Cliente\n"
        for m in self.__mascotas:
            datos += str(m.duenio)+"\n"
            datos += str(m)

        return datos

m = Mascota("Sam")
c = Duenio("Jorge")
m.duenio = c
m1 = Mascota("Loro")
m1.duenio = c
v = Veterinaria("Vete")
v.agregar_mascota(m)
v.agregar_mascota(m1)
print(v)