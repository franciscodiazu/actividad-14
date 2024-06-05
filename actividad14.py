import msvcrt
import os
import csv

personas ={}
clases= [("Lunes y miercoles 9:00 a 10:00 PM Clase de zumba"),
         ("Martes y jueves 10:00 a 12:00 PM Clase de Fit Dance"),
         ("12:00 a 14:00 PM Clase de Abdominales")]
cuposc = [[10]
          [20]
          [20]] 
         
         
         
while True:
    print("<<Presione cualquier tecla para continuar")
    msvcrt.getch()
    os.system("cls")
    print("""\033[35m
     ________________________________________________
    |                                                |
    |    1. Registrar un nuevo usuario.              |
    |    2. Reservar una clase.                      |
    |    3. Consultar clases disponibles.            |
    |    4. Consultar reservas de un usuario.        |
    |    0. Salir del programa                       |
    |________________________________________________|      """)

    opcion= input("Seleccione: ")
    if opcion== "0":
        break
    elif opcion== "1":
        print("\033 34m Registro de Usuario\033[0m")
        id=int(input("Ingrese su ID"))
        if id>0:
            nombre=input("Ingrese Su nombre")
            if len(nombre)>2:
                personas[id]=nombre
                print("\033[32m Usuario Registrado\033[0m")

    elif opcion== "2":
        print("\033 34m Reservar de clases\033[0m")
        id= int(input("Ingrese su ID: "))
        if id in personas:
            for r in range (len(clases)):
                print(f"Clase{r} {clases[i]}: cupos{cuposc[r]}")
    elif opcion== "3":
        print("\033 34m Consultar Clase disponible\033[0m")
    elif opcion== "4":
        print("\033 34m Registro de Usuario\033[0m")
    else:
        print("\033 31m Opcion no valida\033[0m")