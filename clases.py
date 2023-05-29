import csv


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def guardar_datos_csv(self):
        guardar("listado.csv", self)

    def leer_datos_csv(self):
        leer("listado.csv", self)

    def get_marca(self):
        print(self.marca)
    def get_modelo(self):
        print(self.modelo)
    def get_nro_ruedas(self):
        print(self.nro_ruedas)

    def set_marca(self, entrada):
        self.marca = entrada
    def set_modelo(self, entrada):
        self.modelo = entrada
    def set_nro_ruedas(self, entrada):
        self.nro_ruedas = entrada

    def __str__(self):
        return f"Marca: {self.marca}\nModelo:{self.modelo}\n{self.nro_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_velocidad(self):
        print(self.velocidad)
    def get_cilindrada(self):
        print(self.cilindrada)

    def set_velocidad(self, entrada):
        self.velocidad = entrada
    def set_cilindrada(self, entrada):
        self.cilindrada = entrada

    def __str__(self):
        return super().__str__() + f"\n{self.velocidad} km/h\n{self.cilindrada} cc"


class A_particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_asientos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_asientos = nro_asientos

    def get_nro_asientos(self):
        print(self.nro_asientos)

    def set_nro_asientos(self, entrada):
        self.nro_asientos = entrada

    def __str__(self):
        return super().__str__() + f"\nAsientos: {self.nro_asientos}"


class A_carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def get_carga(self):
        print(self.carga)

    def set_carga(self, entrada):
        self.carga = entrada

    def __str__(self):
        return super().__str__() + f"\nCarga: {self.carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def get_tipo(self):
        print(self.tipo)

    def set_tipo(self, entrada):
        self.tipo = entrada

    def __str__(self):
        return super().__str__() + f"\nTipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def get_nro_radios(self):
        print(self.nro_radios)
    def get_cuadro(self):
        print(self.cuadro)
    def get_motor(self):
        print(self.motor)

    def set_nro_radios(self, entrada):
        self.nro_radios = entrada
    def set_cuadro(self, entrada):
        self.cuadro = entrada
    def set_motor(self, entrada):
        self.motor = entrada

    def __str__(self):
        return super().__str__() + f"\nMotor: {self.motor}\nCuadro: {self.cuadro}\nNro. Radios: {self.nro_radios}"



def guardar(nombre_archivo, vehiculo):
    try:
        with open(nombre_archivo, "a", newline="") as archivo:
            datos = [(vehiculo.__class__, vehiculo.__dict__)]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo")
    except Exception as error:
        print('Se ha generado un error no previsto',
        type(error).__name__) 


def leer(nombre_archivo, self):
    try:
        with open(nombre_archivo, "r") as archivo:
            tipo = str(type(self).__name__)
            archivo_csv = csv.reader(archivo)
            print(f"Lista de vehículos tipo {tipo}:")
            for vehiculo in archivo_csv:
                clase, atributos = vehiculo[0], vehiculo[1]
                if clase == f"<class 'clases.{tipo}'>":
                    print(atributos)
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo")
    except Exception as error:
        print('Se ha generado un error no previsto',
        type(error).__name__)
