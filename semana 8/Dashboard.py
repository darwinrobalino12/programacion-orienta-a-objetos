"""" este codigo nos permite navegar dento de las carpetas contenidas en la carpeta principal llamada programacion de objetos"""
import os
import subprocess

def obtener_ruta_base():
    """Obtiene la ruta base del proyecto de manera flexible."""
    return r"C:\Users\petri\PycharmProjects\programacion orientada objetos"

RUTA_BASE = obtener_ruta_base()

def mostrar_codigo(ruta_script):
    """Muestra el contenido del código de un script."""
    try:
        with open(ruta_script, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en una nueva terminal."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Sistemas Unix
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    """Muestra el menú principal del dashboard."""
    unidades = {
        '1': 'deber semana 2',
        '2': 'deber semana 3',
        '3': 'deber semana 4',
        '4': 'Semana 5',
        '5': 'deber semana 6',
        '6': 'deber semana 7',
        '7': 'semana 8',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ").strip()
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(RUTA_BASE, unidades[eleccion_unidad])
            if os.path.isdir(ruta_unidad):  # Validar existencia de la carpeta dentro del arbol dado
                mostrar_sub_menu(ruta_unidad)
            else:
                print(f"Error: La carpeta '{ruta_unidad}' no existe. Por favor, revisa las rutas.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Muestra el submenú de carpetas dentro de una unidad."""
    try:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    except FileNotFoundError:
        print(f"Error: La carpeta '{ruta_unidad}' no existe o no es accesible.")
        return

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        if not sub_carpetas:
            print("No hay subcarpetas disponibles.")
            break

        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ").strip()
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    ruta_sub_carpeta = os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta])
                    mostrar_scripts(ruta_sub_carpeta)
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles en una carpeta específica."""
    try:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    except FileNotFoundError:
        print(f"Error: La carpeta '{ruta_sub_carpeta}' no existe o no es accesible.")
        return

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        if not scripts:
            print("No hay scripts disponibles en esta carpeta.")
            break

        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")

        eleccion_script = input("Elige un script o '0' para regresar: ").strip()
        if eleccion_script == '0':
            break
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ").strip()
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

#gracias