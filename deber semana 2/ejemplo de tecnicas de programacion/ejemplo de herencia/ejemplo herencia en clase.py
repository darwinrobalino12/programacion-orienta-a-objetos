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


            