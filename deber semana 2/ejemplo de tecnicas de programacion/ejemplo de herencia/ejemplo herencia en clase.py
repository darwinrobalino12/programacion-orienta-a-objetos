class Animal:
    # constructor
    def __init__(self, nombre, peso, raza):
        self.nombre = nombre
        self.peso = peso
        self.raza = raza

    def comer(self):
        self.peso += 1

class Dog(Animal):
    pass

class Cat(Animal):
    pass

mi_perro = Dog('Canela', 5, 'runita')
print(mi_perro.nombre)
print(mi_perro.peso)
print(mi_perro.raza)
mi_perro.comer()
print(mi_perro.peso)
