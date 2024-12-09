# Programación Orientada a Objetos (POO)
# iniciamos con una lista vacia para almacenar las temperaturas
class Clima:

# constructor de la clase clima
    def __init__(self):
        self.temperaturas = []
#metodo para ingresar el valor de la temperatura diaria
    def ingresar_temperatura(self, temperatura):
                self.temperaturas.append(temperatura)
                #metodo para calcular el promedio
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)
#funcion que ejecuta el programa
def main():
    clima = Clima()
    print("Ingrese el valor de las temperaturas diarias durante una semana:")
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese el valor de  la temperatura del día {dia}: "))
        clima.ingresar_temperatura(temperatura)
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

if __name__ == "__main__":
    main()

