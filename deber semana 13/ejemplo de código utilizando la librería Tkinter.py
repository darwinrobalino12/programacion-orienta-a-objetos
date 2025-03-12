import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Necesario para manejar imágenes

def mostrar_imagen():
    """Muestra la imagen correspondiente a la opción seleccionada."""
    opcion = opciones_combo.get()
    if opcion == "Manzana":
        imagen = Image.open("Manzana.png")  # Reemplaza con tu imagen
    elif opcion == "Platano":
        imagen = Image.open("Platano.jpg")  # Reemplaza con tu imagen
    elif opcion == "Naranja":
        imagen = Image.open("Naranja.jpg")  # Reemplaza con tu imagen
    elif opcion == "Uva":
        imagen = Image.open("Uva.jpg")# Reemplaza con tu imagen
    else:
        return  # No hacer nada si no hay opción seleccionada

    imagen = imagen.resize((150, 150), Image.LANCZOS)  # Ajusta el tamaño
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk  # Guarda la referencia

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Selector de Imágenes")
ventana.geometry("400x300")

# Lista de opciones
opciones = ["Manzana", "Platano", "Naranja", "Uva"]

# ComboBox para seleccionar opciones
opciones_combo = ttk.Combobox(ventana, values=opciones)
opciones_combo.pack(pady=10)
opciones_combo.current(0)  # Establece la primera opción por defecto

# Botón para mostrar la imagen
boton_mostrar = tk.Button(ventana, text="Mostrar Imagen", command=mostrar_imagen)
boton_mostrar.pack(pady=5)

# Etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()

