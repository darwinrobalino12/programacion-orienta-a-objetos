<<<<<<< HEAD
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
=======
#ejemplo herencia
# Creamos una clase general principal
class Animal:

    def __init__(self, nombre, raza, peso):
        self.nombre = nombre  # Nombre del animal
        self.raza = raza  # Raza del animal
        self.peso = peso  # Peso del animal

    def eat(self):

        # Método que incrementa el peso del animal al comer.

        self.peso += 1


# Clase derivada Dog que hereda de Animal
class Dog(Animal):

    def __init__(self, nombre, raza, peso, sonido):
        # Llamada al constructor de la clase base
        super().__init__(nombre, raza, peso)
        self.sonido = sonido  # Sonido característico del perro


# Clase derivada Cat que hereda de Animal
class Cat(Animal):
   
    def __init__(self, nombre, raza, peso, sonido):
        # Llamada al constructor de la clase base
        super().__init__(nombre, raza, peso)
        self.sonido = sonido  # Sonido característico del gato


# Creación de una instancia de Dog
mi_perro = Dog(nombre="Canela", raza="Runita", peso=10, sonido="Guau")

# Llamada al método eat para que el perro coma y aumente de peso
mi_perro.eat()

# Impresión del peso actual del perro
print(f"El peso de {mi_perro.nombre} después de comer es {mi_perro.peso} kg.")


            
>>>>>>> 35008fae74632dda7ed105a566101eddfb7f32c3
