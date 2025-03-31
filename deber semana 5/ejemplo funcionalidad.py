# Programa que convierte grados centígrados a Fahrenheit
# Este codigo va a recibir una entrada numerica de temperatura en grados centigradoss y la convierte a Fahrenheit.
# Utiliza diferentes tipos de datos: entero (input), flotante (resultado), y cadena (mensajes).

# Definimos la función para conviertir grados centígrados a Fahrenheit
def convertir_a_fahrenheit(grados_centigrados):
    """
    Convierte una temperatura de grados centígrados a Fahrenheit.

    Datos:
    grados_centigrados (float): Temperatura en grados centígrados.

    Retorna:
    float: Temperatura convertida a Fahrenheit, usnado la formula
    """
    grados_fahrenheit = (grados_centigrados * 9 / 5) + 32
    return grados_fahrenheit


# Función principal del programa
def main():
    """
    Función principal que ejecuta el programa.
    Pide al usuario una temperatura en grados centígrados,
    la convierte a Fahrenheit y muestra el resultado.
    """
    # Solicitar al usuario una temperatura en grados centígrados
    grados_centigrados = float(input("Introducir la temperatura en grados centígrados: "))

    # Convertir a Fahrenheit utilizando la función
    grados_fahrenheit = convertir_a_fahrenheit(grados_centigrados)

    # Mostrar el resultado
    print(f"{grados_centigrados} grados centígrados son {grados_fahrenheit} grados Fahrenheit.")


# Llamada a la función principal
if __name__ == "__main__":
    main()


