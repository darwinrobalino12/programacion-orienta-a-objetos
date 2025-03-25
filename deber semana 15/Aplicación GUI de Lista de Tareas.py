import tkinter as tk
from tkinter import ttk, messagebox


# Función para agregar un texto a la lista
def agregar_texto(event=None):
    """Obtiene el texto del campo de entrada y lo agrega a la lista si no está vacío"""
    texto = entrada_texto.get().strip()  # Obtenemos y limpiamos el texto

    if texto:  # Verificamos que no esté vacío
        lista_textos.insert('', tk.END, values=(texto,))  # Agregamos a la tabla
        entrada_texto.delete(0, tk.END)  # Limpiamos el campo
    else:
        messagebox.showwarning("Aviso", "Por favor ingresa texto válido")


# Función para eliminar elemento seleccionado
def eliminar_texto():
    """Elimina el elemento seleccionado de la lista"""
    seleccion = lista_textos.selection()
    if seleccion:  # Si hay algo seleccionado
        lista_textos.delete(seleccion)
    else:
        messagebox.showwarning("Aviso", "Selecciona un elemento para eliminar")


# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    """Muestra confirmación antes de cerrar la aplicación"""
    if messagebox.askokcancel("Salir", "¿Estás seguro de querer salir?"):
        ventana_principal.destroy()


# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Manejador de Textos Mejorado")
ventana_principal.geometry("500x450")  # Aumentamos un poco el tamaño
ventana_principal.configure(bg="lightblue")

# Frame contenedor para mejor organización
frame_principal = tk.Frame(ventana_principal, bg="lightblue")
frame_principal.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Instrucciones para el usuario
etiqueta_instrucciones = tk.Label(
    frame_principal,
    text="Instrucciones:\n1. Escribe texto\n2. Presiona Enter o el botón para agregar\n3. Selecciona y usa el botón para eliminar\n4. Escape para salir",
    font=('Arial', 12),
    justify=tk.LEFT,
    bg="lightblue"
)
etiqueta_instrucciones.pack(pady=5)

# Campo de entrada de texto
entrada_texto = tk.Entry(frame_principal, font=('Arial', 12))
entrada_texto.pack(pady=10, fill=tk.X)
entrada_texto.focus()

# Frame para botones
frame_botones = tk.Frame(frame_principal, bg="lightblue")
frame_botones.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    command=agregar_texto,
    bg="#4CAF50",  # Verde
    fg="white"
)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para eliminar
boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    command=eliminar_texto,
    bg="#f44336",  # Rojo
    fg="white"
)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Tabla para mostrar los textos
lista_textos = ttk.Treeview(
    frame_principal,
    columns=('Texto',),
    show='headings',
    height=10
)
lista_textos.heading('Texto', text='Textos Ingresados')
lista_textos.pack(pady=10, fill=tk.BOTH, expand=True)

# Barra de desplazamiento para la tabla
scrollbar = ttk.Scrollbar(lista_textos, orient="vertical", command=lista_textos.yview)
lista_textos.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Configuración de eventos
entrada_texto.bind('<Return>', agregar_texto)
ventana_principal.bind('<Escape>', cerrar_aplicacion)

ventana_principal.mainloop()