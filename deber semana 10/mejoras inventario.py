import os


# Definir la Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cantidad} unidades - ${self.precio:.2f}"

    def to_dict(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_dict(line):
        id_producto, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))


# Definir la Clase Inventario
class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()  # Cargar productos desde el archivo al iniciar

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()  # Guardar automáticamente los cambios
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        productos_filtrados = [p for p in self.productos if p.id != id_producto]
        if len(productos_filtrados) == len(self.productos):
            print(" Producto no encontrado.")
        else:
            self.productos = productos_filtrados
            self.guardar_inventario()  # Guardar automáticamente los cambios
            print(" Producto eliminado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

    def guardar_inventario(self):
        # Manejo de excepciones al escribir en el archivo
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_dict())
        except PermissionError:
            print("❌ Error: No tienes autorizacion  para escribir en el archivo.")

    def cargar_inventario(self):
        # Verificar si el archivo existe antes de intentar leerlo
        if not os.path.exists(self.ARCHIVO):
            return  # Si el archivo no existe, no hay nada que cargar
        try:
            with open(self.ARCHIVO, "r") as file:
                self.productos = [Producto.from_dict(line) for line in file.readlines()]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        except Exception as e:
            print(f" Error fatal al leer el archivo: {e}")


# Menú de opciones

def menu():
    inventario = Inventario()
    print("\n=== Tienda PEPITO ===")
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Mostrar Inventario\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")

            # Validar que cantidad y precio sean numéricos
            if not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
                print(" Error: Cantidad y precio deben ser valores numéricos.")
                continue

            inventario.agregar_producto(Producto(id_producto, nombre, int(cantidad), float(precio)))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            print("gracias por usar el inventario Saliendo del sistema...")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
