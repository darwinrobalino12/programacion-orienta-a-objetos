class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    # Getter para acceder a la vida
    def obtener_vida(self):
        return self.__vida

    # Setter para modificar la vida
    def modificar_vida(self, vida):
        self.__vida = vida
