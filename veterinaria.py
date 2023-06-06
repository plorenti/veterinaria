class Mascota():
    #Atributo de clase
    id= 0
    listadoMascotas =[]


    def __init__(self,nombre,genero,raza,edad,dueno,mail):
        self.nombre=nombre
        self.genero=genero
        self.raza=raza
        self.edad=edad
        self.dueno=dueno
        self.mail=mail
        self.id = Mascota.id

    def __str__(self):
        return f'El id es {self.id} para {self.nombre}'

    def AgregarMascota(self):
        Mascota.id+=1
        Mascota.listadoMascotas.append(self)


def CrearMascota():
    datos = [input("Ingrese el nombre de la mascota: "),
    input("Ingrese el genero: "),
    input("Ingrese la raza: "),
    int(input("Ingrese edad: ")),
    input("Ingrese el nombre del dueño: "),
    input("Ingrese el mail de contacto: ")
    ]
    return datos


perro = Mascota("Max","Canis","Ovejero aleman",12,"Roberto y Diana","plorenti@gmail.com")
perro.AgregarMascota()
perro = Mascota("Theo","Canis","Ovejero aleman",6,"Roberto y Diana","plorenti@gmail.com")
perro.AgregarMascota()
perro = Mascota("Gina","Canis","Callejera",13,"Roberto y Diana","plorenti@gmail.com")
perro.AgregarMascota()

datos = CrearMascota()
perro = Mascota(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
print(datos)
confirmar = input("Presion 1 si los datos son correctos para guardar")
if(confirmar==1):
    perro.AgregarMascota()



for i in perro.listadoMascotas:
    print(i)


#print(CrearMascota()[0])
