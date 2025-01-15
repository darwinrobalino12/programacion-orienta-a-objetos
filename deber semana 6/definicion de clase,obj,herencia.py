# Definición de la clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Vehículo marca {self.marca}, modelo {self.modelo}"

# Definición de la clase derivada
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        # Llamamos al constructor de la clase base
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima  # Atributo público

    # Método sobrescrito Polimorfismo
    def describir(self):
        return f"Motocicleta marca {self.marca}, modelo {self.modelo}, velocidad máxima {self.velocidad_maxima} km/h"

# Instanciación de objetos
vehiculo = Vehiculo("Toyota", "4runner")
moto = Motocicleta("Honda", "crf230", 125)

# Mostramos las descripciones
print(vehiculo.describir())  # Salida: Vehículo marca Toyota, modelo 4runner
print(moto.describir())      # Salida: Motocicleta marca Honda, modelo crf230, velocidad máxima 125 km/h
