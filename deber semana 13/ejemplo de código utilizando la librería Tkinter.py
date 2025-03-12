import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def agregar_datos():
    """Agrega el nombre y la fruta seleccionada a la lista."""
    nombre = entrada_nombre.get()  # Obtiene el nombre del campo de entrada
    fruta = opciones_combo.get()  # Obtiene la fruta seleccionada del ComboBox
    if nombre and fruta:  # Verifica que ambos campos no estén vacíos
        datos = f"Nombre: {nombre}, Fruta: {fruta}"  # Formatea los datos
        lista_datos.insert(tk.END, datos)  # Inserta los datos en la lista
        entrada_nombre.delete(0, tk.END)  # Limpia el campo de nombre

def limpiar_lista():
    """Limpia todos los elementos de la lista."""
    lista_datos.delete(0, tk.END)  # Elimina todos los elementos de la lista

def mostrar_imagen():
    """Muestra la imagen correspondiente a la opción seleccionada."""
    opcion = opciones_combo.get()
    if opcion == "Manzana":
        imagen = Image.open("Manzana.png")
    elif opcion == "Plátano":
        imagen = Image.open("Platano.jpg")
    elif opcion == "Naranja":
        imagen = Image.open("Naranja.jpg")
    elif opcion == "Uva":
        imagen = Image.open("Uva.jpg")
    else:
        return

    imagen = imagen.resize((150, 150), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación GUI")
ventana.geometry("500x400")

# Componentes para ingresar nombre
etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_nombre.pack(pady=5)

entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Componentes para seleccionar fruta
opciones = ["Manzana", "Plátano", "Naranja", "Uva"]

opciones_combo = ttk.Combobox(ventana, values=opciones)
opciones_combo.pack(pady=5)
opciones_combo.current(0)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar Datos", command=agregar_datos)
boton_agregar.pack(pady=5)

# Lista para mostrar datos agregados
lista_datos = tk.Listbox(ventana, height=5, width=50)  # Aumenta el ancho de la lista
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Componentes para mostrar imagen
boton_mostrar = tk.Button(ventana, text="Mostrar Imagen", command=mostrar_imagen)
boton_mostrar.pack(pady=5)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()



