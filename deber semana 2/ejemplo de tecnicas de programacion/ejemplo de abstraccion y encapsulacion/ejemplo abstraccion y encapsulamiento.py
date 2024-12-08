class Animal:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def hacer_ruido(self):
        print(f"{self.get_nombre()} hace un sonido.")

    def comer(self):
        print(f"{self.get_nombre()} está comiendo.")

class Mamifero(Animal):
    def amamantar(self):
        print(f"{self.get_nombre()} está amamantando.")

class Perro(Mamifero):
    def jugar_a_buscar(self):
        print(f"{self.get_nombre()} está jugando a buscar.")

class Gato(Mamifero):
    def trepar(self):
        print(f"{self.get_nombre()} está trepando.")

class Pajaro(Animal):
    def volar(self):
        print(f"{self.get_nombre()} está volando.")

# Creamos una lista de animales
animales = [Perro("Canela", "Runita"), Gato("Pelusa", "Siamés"), Pajaro("Piolin", "Canario")]

# Recorremos la lista y hacemos que cada animal haga ruido
for animal in animales:
    animal.hacer_ruido()

# Ejemplo de función polimórfica
def alimentar(animal):
    print(f"Estamos alimentando a {animal.get_nombre()}.")
    animal.comer()

# Llamamos a la función alimentar con diferentes animales
alimentar(animales[0])  # Alimenta al perro
alimentar(animales[1])  # Alimenta al gato
alimentar(animales[2])  # Alimenta al pájaro

















