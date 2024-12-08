#poliformismo
class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def hacer_ruido(self):
        print(f"{self.nombre} hace un sonido.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def hacer_ruido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_ruido(self):
        print("¡Miau!")

class Pajaro(Animal):
    def hacer_ruido(self):
        print("¡Pío!")

# Creamos una lista de animales
animales = [Perro("Canela", "Runita"), Gato("Pelusa", "Siamés"), Pajaro("Piolin", "Canario")]

# Recorremos la lista y hacemos que cada animal haga ruido
for animal in animales:
    animal.hacer_ruido()

# Ejemplo de función polimorfica
def alimentar(animal):
    print(f"Estamos dandoles de comer a {animal.nombre}.")
    animal.comer()

# Llamamos a la función alimentar con diferentes animales
alimentar(animales[0])  # Alimenta al perro
alimentar(animales[1])  # Alimenta al gato
alimentar(animales[2]) # Alimenta a piolin