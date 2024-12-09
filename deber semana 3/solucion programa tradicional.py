# Programación Tradicional
# Función para ingresar las temperaturas diarias durante la semana
def ingresar_temperaturas():

    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día tomada al mismo horario {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio de la semana
def calcular_promedio(temperaturas):
    """Función para calcular el promedio de las temperaturas semanales."""
    return sum(temperaturas) / len(temperaturas)

# Función que ejecuta el programa
def main():

    print("Ingrese las temperaturas diarias durante una semana:")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

if __name__ == "__main__":
    main()




