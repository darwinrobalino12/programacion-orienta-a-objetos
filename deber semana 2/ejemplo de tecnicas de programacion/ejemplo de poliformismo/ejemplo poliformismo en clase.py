#polimorfismo
# Clase principal Animal
class Animal:
    """
    Clase base que representa un animal genérico.
    Atributos:
        - nombre: Nombre del animal.
    Métodos:
        - hacer_sonido: Método genérico que debe ser implementado en las clases derivadas.
    """
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del animal

    def hacer_sonido(self):
        """
        Método genérico para emitir un sonido.
        Este método debe ser sobrescrito en las clases hijas.
        """
        raise NotImplementedError("El método 'hacer_sonido' debe ser implementado por las clases hijas.")


# Clase derivada Dog
class Dog(Animal):
    """
    Clase que representa a un perro, hereda de Animal.
    Atributos:
        - raza: Raza del perro.
    Métodos:
        - hacer_sonido: Sobrescribe el método base para emitir el sonido de un perro.
    """
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.raza = raza  # Raza del perro

    def hacer_sonido(self):
        """
        Método sobrescrito para emitir el sonido característico de un perro.
        """
        return f"{self.nombre} ({self.raza}) dice: GUAU"


# Clase derivada Cat
class Cat(Animal):
    """
    Clase que representa a un gato, hereda de Animal.
    Atributos:
        - sonido: Sonido característico del gato (por defecto 'MIAU').
    Métodos:
        - hacer_sonido: Sobrescribe el método base para emitir el sonido de un gato.
    """
    def __init__(self, nombre, sonido="MIAU"):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.sonido = sonido  # Sonido característico del gato

    def hacer_sonido(self):
        """
        Método sobrescrito para emitir el sonido característico de un gato.
        """
        return f"{self.nombre} dice: {self.sonido}"


# Función que aplica polimorfismo
def mostrar_sonido(animal):
    """
    Función que recibe un objeto de tipo Animal y muestra el sonido que emite.
    Este es un ejemplo de polimorfismo, ya que el comportamiento varía según la clase del objeto.
    """
    print(animal.hacer_sonido())


# Crear objetos
mi_perro = Dog(nombre="Canela", raza="Runita")
mi_gato = Cat(nombre="Pelusa")

# Uso del polimorfismo
mostrar_sonido(mi_perro)  # Salida: Canela (Runita) dice: GUAU
mostrar_sonido(mi_gato)   # Salida: Pelusa dice: MIAU
