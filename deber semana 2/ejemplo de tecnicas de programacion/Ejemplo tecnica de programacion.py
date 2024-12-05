class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class GuerreroModerno(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma, chaleco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma
        self.chaleco = chaleco

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Pistola, daño 10. (2) Bazuca, daño 30."))
        if opcion == 1:
            self.arma = 10
        elif opcion == 2:
            self.arma = 30
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Arma:", "Pistola" if self.arma == 10 else "Bazuca" if self.arma == 30 else "No definida")
        print("·Chaleco antibalas:", self.chaleco)

    def daño(self, enemigo):
        return self.fuerza * self.arma - enemigo.defensa * self.chaleco


class GuerreroDefensivo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma, chaleco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma
        self.chaleco = chaleco

    def atributos(self):
        super().atributos()
        print("·Arma:", "Pistola" if self.arma == 10 else "Bazuca" if self.arma == 30 else "No definida")
        print("·Chaleco antibalas:", self.chaleco)

    def daño(self, enemigo):
        return self.fuerza * self.arma - (enemigo.defensa * self.chaleco)


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")  # Nueva ronda para el otro jugador
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Creación de los personajes con armas modernas y chalecos antibalas
personaje_1 = GuerreroModerno("Bryan", 15, 8, 6, 120, 10, 1)  # Bryan con pistola (daño 10) y chaleco antibalas
personaje_2 = GuerreroDefensivo("Kimberly", 12, 9, 8, 110, 30, 1)  # Kimberly con bazuca (daño 30) y chaleco antibalas

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
