class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def hacer_ruido(self):
        print("¡Hace un sonido!")

class Perro(Animal):
    def hacer_ruido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_ruido(self):
        print("¡Miau!")

# Creamos un perro y un gato
mi_perro = Perro("Canela", "Runita")
mi_gato = Gato("Pelusa", "Siamés")

# Hacemos que nuestros animales hagan cosas
print(f"Mi perro se llama {mi_perro.nombre} y es un {mi_perro.raza}.")
mi_perro.comer()
mi_perro.hacer_ruido()

print(f"Mi gato se llama {mi_gato.nombre} y es un {mi_gato.raza}.")
mi_gato.comer()
mi_gato.hacer_ruido()