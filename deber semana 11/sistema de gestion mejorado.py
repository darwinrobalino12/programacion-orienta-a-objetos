import os


# Función para limpiar la pantalla de la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# Definir la Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un objeto Producto con sus atributos."""
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.id} - {self.nombre} - {self.cantidad} unidades - ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto a una cadena para guardar en el archivo."""
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_dict(line):
        """Crea un producto a partir de una línea leída del archivo."""
        id_producto, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))


# Definir la Clase Inventario
class Inventario:
    ARCHIVO = "inventario.txt"  # Nombre del archivo para guardar el inventario

    def __init__(self):
        """Inicializa el inventario y carga los productos desde el archivo."""
        self.productos = []
        self.cargar_inventario()  # Cargar productos desde el archivo al iniciar

    def agregar_producto(self, producto):
        """Agrega un producto al inventario, verificando duplicados y guardando cambios."""
        # Verificar si el ID ya existe ANTES de añadir el producto
        if any(p.id == producto.id for p in self.productos):
            print("❌ Error: El ID del producto ya existe.")
            return  # Salir de la función si el ID está duplicado

        self.productos.append(producto)
        self.guardar_inventario()  # Guardar automáticamente los cambios
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID y guarda los cambios."""
        productos_filtrados = [p for p in self.productos if p.id != id_producto]
        if len(productos_filtrados) == len(self.productos):
            print("Producto no encontrado.")
        else:
            self.productos = productos_filtrados
            self.guardar_inventario()  # Guardar automáticamente los cambios
            print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto existente."""
        for producto in self.productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print("✅ Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """Busca y muestra productos por nombre."""
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if not productos_encontrados:
            print("No se encontraron productos con ese nombre.")
        else:
            for producto in productos_encontrados:
                print(producto)

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\nID\tNombre\tCantidad\tPrecio")
            print("-" * 40)
            for p in self.productos:
                print(f"{p.id}\t{p.nombre}\t{p.cantidad}\t\t${p.precio:.2f}")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_dict())
        except PermissionError:
            print("❌ Error: No tienes autorización para escribir en el archivo.")

    def cargar_inventario(self):
        """Carga el inventario desde el archivo."""
        if not os.path.exists(self.ARCHIVO):
            return  # Si el archivo no existe, no hay nada que cargar
        try:
            with open(self.ARCHIVO, "r") as file:
                self.productos = [Producto.from_dict(line) for line in file.readlines()]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        except Exception as e:
            print(f"Error fatal al leer el archivo: {e}")


# Menú de opciones
def menu():
    inventario = Inventario()
    print("\n=== NOVEDADES ELECTRONICAS  PEPITO ===")
    opciones = [
        "Agregar Producto",
        "Eliminar Producto",
        "Actualizar Producto",
        "Buscar Producto",
        "Mostrar Inventario",
        "Salir"
    ]

    while True:
        print("\nSeleccione una opción:")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        opcion = input("Opción: ")

        if opcion.isdigit() and 1 <= int(opcion) <= len(opciones):
            opcion_elegida = opciones[int(opcion) - 1]

            if opcion_elegida == "Agregar Producto":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = input("Cantidad: ")
                precio = input("Precio: ")

                if not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
                    print("Error: Cantidad y precio deben ser valores numéricos.")
                    continue

                producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                inventario.agregar_producto(producto)

            elif opcion_elegida == "Eliminar Producto":
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion_elegida == "Actualizar Producto":
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
                precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
                inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                               float(precio) if precio else None)

            elif opcion_elegida == "Buscar Producto":
                nombre = input("Nombre del producto a buscar: ")
                inventario.buscar_producto_por_nombre(nombre)

            elif opcion_elegida == "Mostrar Inventario":
                inventario.mostrar_inventario()

            elif opcion_elegida == "Salir":
                print("Saliendo del sistema te esperamos pronto...")
                break

            limpiar_pantalla()
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()