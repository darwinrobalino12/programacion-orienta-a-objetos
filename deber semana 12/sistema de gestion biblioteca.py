# Clase Libro: Representa un libro con título, autor, categoría e ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.categoria = categoria  # Categoría del libro
        self.isbn = isbn  # ISBN para identificar el libro

    def __str__(self):
        """Devuelve una descripción del libro"""
        return f"{self.titulo} por {self.autor}, Categoria: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario: Representa a un usuario de la biblioteca con ID único y libros prestados
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre  # Nombre del usuario
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        """Devuelve información del usuario"""
        return f"{self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca: Representa la biblioteca que gestiona los libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar los libros por ISBN
        self.usuarios = {}  # Diccionario para almacenar los usuarios por ID
        self.cargar_libros()  # Cargar los libros del archivo al iniciar el programa
        self.cargar_usuarios()  # Cargar los usuarios del archivo al iniciar el programa

    def agregar_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        self.libros[libro.isbn] = libro
        self.guardar_libros()  # Guardar libros en el archivo

    def quitar_libro(self, isbn):
        """Eliminar un libro de la biblioteca"""
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()  # Guardar los cambios en el archivo
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def agregar_usuario(self, usuario):
        """Añadir un usuario a la biblioteca"""
        self.usuarios[usuario.id_usuario] = usuario
        self.guardar_usuarios()  # Guardar usuarios en el archivo

    def quitar_usuario(self, id_usuario):
        """Eliminar un usuario de la biblioteca"""
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_usuarios()  # Guardar los cambios en el archivo
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("El usuario no se encuentra en la biblioteca.")

    def prestar_libro(self, id_usuario, isbn):
        """Prestar un libro a un usuario"""
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"El libro {libro.titulo} ha sido prestado a {usuario.nombre}.")
                self.guardar_usuarios()  # Guardar cambios de los usuarios
            else:
                print(f"{usuario.nombre} ya tiene prestado el libro {libro.titulo}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Devolver un libro prestado por un usuario"""
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.get(isbn)
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"{usuario.nombre} ha devuelto el libro {libro.titulo}.")
                self.guardar_usuarios()  # Guardar cambios de los usuarios
            else:
                print(f"{usuario.nombre} no tiene prestado el libro {libro.titulo}.")
        else:
            print("Usuario no encontrado.")

    def mostrar_libros(self):
        """Mostrar todos los libros en la biblioteca"""
        if self.libros:
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def mostrar_usuarios(self):
        """Mostrar todos los usuarios registrados en la biblioteca"""
        if self.usuarios:
            for usuario in self.usuarios.values():
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def mostrar_libros_prestados(self, id_usuario):
        """Mostrar todos los libros prestados a un usuario"""
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

    def guardar_libros(self):
        """Guardar todos los libros en un archivo"""
        with open("inventario_biblioteca.txt", "w") as archivo:
            for libro in self.libros.values():
                archivo.write(f"{libro.titulo},{libro.autor},{libro.categoria},{libro.isbn}\n")
        print("Inventario de libros guardado.")

    def cargar_libros(self):
        """Cargar los libros desde el archivo al inicio del programa"""
        try:
            with open("inventario_biblioteca.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    libro = Libro(datos[0], datos[1], datos[2], datos[3])
                    self.libros[libro.isbn] = libro
            print("Libros cargados desde el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo de inventario. Se creará uno nuevo.")

    def guardar_usuarios(self):
        """Guardar todos los usuarios en un archivo"""
        with open("usuarios_biblioteca.txt", "w") as archivo:
            for usuario in self.usuarios.values():
                archivo.write(f"{usuario.nombre},{usuario.id_usuario}\n")
        print("Usuarios guardados.")

    def cargar_usuarios(self):
        """Cargar los usuarios desde el archivo al inicio del programa"""
        try:
            with open("usuarios_biblioteca.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    usuario = Usuario(datos[0], datos[1])
                    self.usuarios[usuario.id_usuario] = usuario
            print("Usuarios cargados desde el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios. Se creará uno nuevo.")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Mostrar libros")
    print("4. Agregar usuario")
    print("5. Eliminar usuario")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Mostrar usuarios")
    print("9. Mostrar libros prestados")
    print("10. Salir")

# Función principal que ejecuta el sistema
def ejecutar_sistema():
    biblioteca = Biblioteca()  # Crear una instancia de la biblioteca

    while True:
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input("Elige una opción (1-10): ")

        if opcion == "1":
            # Agregar un libro
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            # Eliminar un libro
            isbn = input("Ingresa el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Mostrar todos los libros
            biblioteca.mostrar_libros()

        elif opcion == "4":
            # Agregar un usuario
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.agregar_usuario(usuario)

        elif opcion == "5":
            # Eliminar un usuario
            id_usuario = input("Ingresa el ID del usuario a eliminar: ")
            biblioteca.quitar_usuario(id_usuario)

        elif opcion == "6":
            # Prestar un libro
            id_usuario = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "7":
            # Devolver un libro
            id_usuario = input("Ingresa el ID del usuario: ")
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "8":
            # Mostrar todos los usuarios
            biblioteca.mostrar_usuarios()

        elif opcion == "9":
            # Mostrar libros prestados por un usuario
            id_usuario = input("Ingresa el ID del usuario para ver los libros prestados: ")
            biblioteca.mostrar_libros_prestados(id_usuario)

        elif opcion == "10":
            # Salir del programa
            print("Saliendo del sistema. ¡Adiós!")
            break

        else:
            print("Opción no válida, por favor elige una opción entre 1 y 10.")

# Ejecutar el sistema si es el script principal
if __name__ == "__main__":
    ejecutar_sistema()
