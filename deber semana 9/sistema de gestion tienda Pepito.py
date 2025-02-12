# Definir  Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cantidad} unidades - ${self.precio:.2f}"


# definimos la Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id != id_producto]
        print("Producto eliminado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)


# creamos un menú simple
def menu():
    inventario = Inventario()
    print("\n=== Tienda PEPITO ===")
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Mostrar Inventario\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            inventario.mostrar_inventario()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
