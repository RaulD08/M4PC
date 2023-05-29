from clases import *


instancias = []

n = int(input("Cuántos vehículos desea ingresar?: "))
for i in range(n):
    print("Ingreso los datos del vehículo", i+1)
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    nro_ruedas = input("Ingrese el número de ruedas: ")
    velocidad = input("Ingrese la velocidad en km/h: ")
    cilindrada = input("Ingrese la cilindrada en cc: ")

    instancias.append(Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada))
    print("")

print("-----------------------")
print("Imprimiendo lista de vehículos:")
print("")
for index, i in enumerate(instancias):
    print(f"Datos del vehículo {index+1}:")
    print(i)
    print("")
