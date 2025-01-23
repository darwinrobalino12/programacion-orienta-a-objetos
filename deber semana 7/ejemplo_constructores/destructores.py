# Clase Persona: Demostración de constructores (__init__) y destructores (__del__)
class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor: Inicializa los atributos de la clase Persona.
        Este método se ejecuta automáticamente al crear una instancia de la clase.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado a una persona llamada {self.nombre}, de {self.edad} años.")

    def saludar(self):
        #se crea un metodo para saludar
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """
        Destructor: Limpia los recursos asociados a la clase.       """
        print(f"El objeto de {self.nombre} ha sido eliminado de la memoria.")


# Bloque principal del programa
if __name__ == "__main__":
    # Crear una instancia de la clase Persona
    persona1 = Persona("Darwin", 42)
    persona1.saludar()

    # Crear otra instancia
    persona2 = Persona("Anita", 38)
    persona2.saludar()

    # Fin del programa: Aquí se activará automáticamente el destructor para los objetos restantes.
    print("Fin del programa.")

