from clases import *


particular = A_particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = A_carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva", 21,"Doble Viga", "2T")

print("-----------------------")
print(particular)
print("-----------------------")
print(carga)
print("-----------------------")
print(bicicleta)
print("-----------------------")
print(motocicleta)
print("-----------------------")


print("Motocicleta es instancia con relación a Vehículo: " + str(isinstance(motocicleta, Vehiculo)))
print("Motocicleta es instancia con relación a Automovil: " + str(isinstance(motocicleta, Automovil)))
print("Motocicleta es instancia con relación a Vehículo particular: " + str(isinstance(motocicleta, A_particular)))
print("Motocicleta es instancia con relación a Vehículo de Carga: " + str(isinstance(motocicleta, A_carga)))
print("Motocicleta es instancia con relación a Bicicleta: " + str(isinstance(motocicleta, Bicicleta)))
print("Motocicleta es instancia con relación a Motocicleta: " + str(isinstance(motocicleta, Motocicleta)))