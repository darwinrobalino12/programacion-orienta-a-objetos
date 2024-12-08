class Persona:
    # constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre},{self.apellido}, y mi edad en anos es {self.edad}")

# Instanciar objetos
persona = Persona(nombre='Juan', apellido='Jerez', edad='20')
persona2 = Persona(nombre='Jose', apellido='Perez', edad='25')

# Imprimir atributos
print(persona.nombre)
print(persona.apellido)
print(persona.edad)
print(persona2.nombre)

# Uso de los métodos
persona.saludar()
persona2.saludar()
#imprimir
print(persona.nombre)