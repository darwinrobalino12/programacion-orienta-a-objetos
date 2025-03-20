import tkinter as tk  # Importamos la librería tkinter
from tkinter import ttk  # Importamos ttk (Themed Tkinter) para componentes con mejor apariencia
from tkcalendar import DateEntry  # Importamos DateEntry de tkcalendar s
import os  # Importamos el módulo os para trabajar con archivos

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Mi Agenda Personal")  # Le ponemos un título a la ventana
ventana.geometry("600x400")  # Definimos el tamaño inicial de la ventana (ancho x alto)
ventana.configure(bg="lightblue")  # Cambiamos el color de fondo de la ventana a azul claro

# Creamos un Frame (contenedor) para la lista de eventos
frame_lista = ttk.Frame(ventana)
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Lo empaquetamos y lo hacemos expandible

# Creamos un Frame para la entrada de datos (fecha, hora, descripción)
frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=10, padx=10)

# Creamos un Frame para los botones (Agregar, Eliminar, Salir)
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10, padx=10)

# Creamos un Treeview (lista) para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")  # Nombramos la columna "Fecha"
tree.heading("Hora", text="Hora")  # Nombramos la columna "Hora"
tree.heading("Descripción", text="Descripción")  # Nombramos la columna "Descripción"
tree.pack(fill=tk.BOTH, expand=True)  # Lo hacemos expandible

# Creamos etiquetas para los campos de entrada
ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)

# Creamos un DateEntry (calendario) para seleccionar la fecha
entrada_fecha = DateEntry(frame_entrada, width=12, background='darkblue',
                        foreground='white', borderwidth=2)
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)  # Lo ubicamos en la fila 0, columna 1

# Creamos un Entry (campo de texto) para ingresar la hora
entrada_hora = ttk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=5, pady=5)  # Lo ubicamos en la fila 1, columna 1

# Creamos un Entry para ingresar la descripción
entrada_descripcion = ttk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)  # Lo ubicamos en la fila 2, columna 1

# Creamos los botones
boton_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=lambda: agregar_evento())
boton_agregar.pack(side=tk.LEFT, padx=5)  # Lo empaquetamos a la izquierda

boton_eliminar = ttk.Button(frame_botones, text="Eliminar Evento", command=lambda: eliminar_evento())
boton_eliminar.pack(side=tk.LEFT, padx=5)  # Lo empaquetamos a la izquierda

boton_salir = ttk.Button(frame_botones, text="Salir", command=ventana.quit)
boton_salir.pack(side=tk.LEFT, padx=5)  # Lo empaquetamos a la izquierda

# Función para agregar un evento
def agregar_evento():
    fecha = entrada_fecha.get_date()  # Obtenemos la fecha del calendario
    hora = entrada_hora.get()  # Obtenemos la hora del campo de texto
    descripcion = entrada_descripcion.get()  # Obtenemos la descripción del campo de texto
    if not validar_hora(hora):  # Validamos la hora
        return  # Si no es válida, salimos de la función
    tree.insert("", tk.END, values=(fecha, hora, descripcion))  # Insertamos el evento en el Treeview
    guardar_eventos()  # Guardamos los eventos después de agregar uno
    entrada_fecha.delete(0, tk.END)  # Limpiamos el campo de fecha
    entrada_hora.delete(0, tk.END)  # Limpiamos el campo de hora
    entrada_descripcion.delete(0, tk.END)  # Limpiamos el campo de descripción

# Función para eliminar un evento
def eliminar_evento():
    item_seleccionado = tree.selection()  # Obtenemos el ítem seleccionado del Treeview
    if item_seleccionado:
        tree.delete(item_seleccionado)  # Lo eliminamos
        guardar_eventos()  # Guardamos los eventos después de eliminar uno

# Función para validar la hora
def validar_hora(hora):
    try:
        horas, minutos = map(int, hora.split(':'))  # Separamos horas y minutos
        if 0 <= horas <= 23 and 0 <= minutos <= 59:  # Verificamos si están en el rango correcto
            return True
        else:
            return False
    except ValueError:  # Si hay un error al convertir a entero, la hora no es válida
        return False

# Función para guardar los eventos en un archivo
def guardar_eventos():
    with open("agenda.txt", "w") as archivo:  # Abrimos el archivo "agenda.txt" en modo escritura
        for item in tree.get_children():  # Recorremos los ítems del Treeview
            fecha, hora, descripcion = tree.item(item, "values")  # Obtenemos los valores del ítem
            archivo.write(f"{fecha},{hora},{descripcion}\n")  # Escribimos los valores en el archivo, separados por comas

# Función para cargar los eventos desde un archivo
def cargar_eventos():
    if os.path.exists("agenda.txt"):  # Verificamos si el archivo "agenda.txt" existe
        with open("agenda.txt", "r") as archivo:  # Abrimos el archivo en modo lectura
            for linea in archivo:  # Recorremos las líneas del archivo
                fecha, hora, descripcion = linea.strip().split(",")  # Separamos los valores de la línea
                tree.insert("", tk.END, values=(fecha, hora, descripcion))  # Insertamos los valores en el Treeview

cargar_eventos()  # Cargamos los eventos al iniciar la aplicación

ventana.mainloop()  # Iniciamos el bucle principal de la aplicación