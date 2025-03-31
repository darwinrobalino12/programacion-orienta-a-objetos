<<<<<<< HEAD
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, mana):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.mana = mana

    def lanzar_hechizo(self, enemigo):
        if self.mana >= 10:
            enemigo.vida -= self.inteligencia * 2
            self.mana -= 10
            print(self.nombre, "ha lanzado un hechizo a", enemigo.nombre)
        else:
            print(self.nombre, "no tiene suficiente mana")
=======
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, mana):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.mana = mana

    def lanzar_hechizo(self, enemigo):
        if self.mana >= 10:
            enemigo.vida -= self.inteligencia * 2
            self.mana -= 10
            print(self.nombre, "ha lanzado un hechizo a", enemigo.nombre)
        else:
            print(self.nombre, "no tiene suficiente mana")
>>>>>>> 35008fae74632dda7ed105a566101eddfb7f32c3
