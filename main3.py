from clases import *


automovil1 = Automovil("Toyota", "Yaris", 4, 120, 800)
automovil2 = Automovil("Fiat", "Palio", 4, 95, 1200)
automovil3 = Automovil("Ford", "Fiesta", 4, 125, 1500)

particular = A_particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = A_carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva", 21,"Doble Viga", "2T")


automovil1.guardar_datos_csv()
automovil2.guardar_datos_csv()
automovil3.guardar_datos_csv()
carga.guardar_datos_csv()
particular.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()


automovil1.leer_datos_csv()
print("-----------------------")
carga.leer_datos_csv()
print("-----------------------")
particular.leer_datos_csv()
print("-----------------------")
bicicleta.leer_datos_csv()
print("-----------------------")
motocicleta.leer_datos_csv()