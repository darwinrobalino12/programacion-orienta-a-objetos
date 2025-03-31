import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'deber semana 2/ejemplo de tecnicas de programacion/deber semana 3/solucion programa tradicional.py',
        '2': 'deber semana 2/ejemplo de tecnicas de programacion/deber semana 3/solucion programacion orientada objetos.py',
        '3': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de abstraccion y encapsulacion/ejemplo.py',
        '4': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de abstraccion y encapsulacion/ejemplo abstraccion y encapsulamiento.py',
        '5': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de abstraccion y encapsulacion/ejemplo clase.py',
        '6': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de abstraccion y encapsulacion/ejemplo en clase.py' ,
        '7': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de herencia/ejemplo.py',
        '8': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de herencia/ejemplo herencia en clase.py',
        '9': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de poliformismo/ejemplo.py',
        '10': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de poliformismo/ejemplo poliformismo.py',
        '11': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de poliformismo/ejemplo poliformismo en clase.py',
        '12': 'deber semana 2/ejemplo de tecnicas de programacion/ejemplo de poliformismo/Ejemplo tecnica de programacion.py',
        '13': 'deber semana 3/solucion programa tradicional.py',
        '14': 'deber semana 3/solucion programacion orientada objetos.py' ,
        '15': 'deber semana 4/ejemplo mundo real.py' ,
        '16': 'deber semana 6/definicion de clase,obj,herencia.py',
        '17': 'deber semana 7/ejemplo_constructores/destructores.py',
        '18': 'semana 5/ejemplo funcionalidad.py',
        '19': 'deber semana 8/Dashboard1.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()