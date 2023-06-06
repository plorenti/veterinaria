import os
'''
Desarrollado por Pablo Lorenti para una tarea de Codo a Codo

'''
class Mascota():
    #Atributo de clase
    id= 0
    listadoMascotas =[]


    def __init__(self,nombre,especie,raza,edad,dueno,telefono):
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.dueno=dueno
        self.telefono=telefono
        self.id = Mascota.id

    def __str__(self):
        return f'ID: {self.id} - Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad} - Nombre del dueño: {self.dueno} - Telefono: {self.telefono}'

    def AgregarMascota(self):
        Mascota.id+=1
        Mascota.listadoMascotas.append(self)

mascota = Mascota("","","","","","")

def DatosMascotaNueva():
    '''
    Valida la información ingresada por el usuario
    Devuelte una lista con los datos para crear el objeto Mascota
    '''
    print("Ingrese los datos de la mascota o para volver al menu principal presione X")
    print("-"*75)
    valido = True
    datos=[]
    nombre =''
    especie =''
    raza=''
    edad=''
    dueno=''
    telefono=''    
    
    while len(nombre)<=0:            
        nombre = input("Ingrese el nombre de la mascota: ")
        if nombre == "x" or nombre =="X":
            print("Salir")
            valido=False
            break
        datos.append(nombre)


    while len(especie)<=0 and valido:            
        especie = input("Ingrese especie: ")
        if especie == "x" or especie =="X":
            print("Salir 2")
            valido=False
            break
        datos.append(especie)

    while len(raza)<=0 and valido:
        raza = input("Ingrese raza: ")
        if raza == "x" or raza =="X":
            print("Salir")
            valido=False
            break
        datos.append(raza)

    while len(edad)<=0 and valido:
        edad = input("Ingrese edad: ")
        if edad == "x" or edad =="X":
            print("Salir")
            valido=False
            break
        
        datos.append(edad)
        

    while len(dueno)<=0 and valido:
        dueno = input("Ingrese nombre del dueño: ")
        if dueno == "x" or dueno =="X":
            print("Salir")
            valido=False
            break
        
        datos.append(dueno)

    while len(telefono)<=0 and valido:
        telefono = input("Ingrese telefono de contacto: ")
        if telefono == "x" or telefono =="X":
            print("Salir")
            valido=False
            break
        
        datos.append(telefono)

    if valido:
        return datos
    else:
        datos.clear()
        return False

def CrearMascota():
    datos = DatosMascotaNueva()

    #print(datos)

    if datos != False:
        confirmar = input("Presion 1 si los datos son correctos para guardar: ")
        if(confirmar=="1"):
            mascota = Mascota(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
            mascota.AgregarMascota()

def ListarMascotas():
    for i in mascota.listadoMascotas:
        print(i)
    input("Presione una tecla para volver al menu principal")

def MenuPrincipal():
    '''Funcion que muestra las opciones del menu y avanza segun
    la seleccion del usuario.'''
    opciones=["1)Agregar Mascota","2)Consultar Mascota","3)Editar Mascota","4)Eliminar Mascota","5)Listar Mascotas","6)Salir"]
    for i in opciones:
      print(i)

    opcion = int(input("Ingrese una opcion: "))
    if opcion==1:
        print("Opcion1")
        CrearMascota()
        
    elif opcion==2:
        print("No implementado")
        input("Presione una tecla para continuar")
    elif opcion==3:
        print("No implementado")
        input("Presione una tecla para continuar")
    elif opcion==4:
        print("No implementado")
        input("Presione una tecla para continuar")
    elif opcion==5:
        ListarMascotas()       
       
        
    else:
        print("salir")
        exit()

def Programa():
    while True:
        os.system("cls")
        MenuPrincipal()  
         
Programa()


