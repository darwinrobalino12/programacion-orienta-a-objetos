<<<<<<< HEAD
class GuerreroMagico(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, magia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.magia = magia

    def daño(self, enemigo):
        # Implementación polimórfica del daño, usando magia en vez de fuerza
        return self.magia * 3 - enemigo.defensa
=======
class GuerreroMagico(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, magia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.magia = magia

    def daño(self, enemigo):
        # Implementación polimórfica del daño, usando magia en vez de fuerza
        return self.magia * 3 - enemigo.defensa

>>>>>>> 35008fae74632dda7ed105a566101eddfb7f32c3
