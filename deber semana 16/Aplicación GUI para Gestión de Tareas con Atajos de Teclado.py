import tkinter as tk
from tkinter import ttk, messagebox


class GestorTareas:
    def __init__(self, ventana):
        # Configuración inicial de la ventana
        self.ventana = ventana
        self.ventana.title("Mi Gestor de Tareas")
        self.ventana.geometry("400x400")
        self.ventana.configure(bg="lightblue")

        # Crear los elementos de la interfaz
        self.crear_interfaz()

        # Configurar los atajos de teclado
        self.configurar_atajos()

    def crear_interfaz(self):
        """Crea todos los elementos visuales de la aplicación"""
        # Campo para escribir nuevas tareas
        self.etiqueta = ttk.Label(self.ventana, text="Escribe tu tarea:")
        self.etiqueta.pack(pady=5)

        self.entrada_tarea = ttk.Entry(self.ventana, width=40)
        self.entrada_tarea.pack(pady=5)
        self.entrada_tarea.focus()  # El cursor aparece aquí al iniciar

        # Botones para las acciones
        self.boton_agregar = ttk.Button(self.ventana, text="Agregar", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = ttk.Button(self.ventana, text="Completar", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.ventana, text="Eliminar", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista donde se muestran las tareas
        self.lista_tareas = tk.Listbox(self.ventana, width=50, height=15)
        self.lista_tareas.pack(pady=10)

        # Etiqueta para mostrar el estado
        self.contador = ttk.Label(self.ventana, text="Tareas: 0")
        self.contador.pack()

    def configurar_atajos(self):
        """Asigna teclas para realizar acciones rápidamente"""
        self.entrada_tarea.bind("<Return>", lambda e: self.agregar_tarea())
        self.ventana.bind("<c>", lambda e: self.marcar_completada())
        self.ventana.bind("<d>", lambda e: self.eliminar_tarea())
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())

    def agregar_tarea(self):
        """Añade una nueva tarea a la lista"""
        tarea = self.entrada_tarea.get().strip()
        if tarea:  # Solo agregar si hay texto
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo
            self.actualizar_contador()
        else:
            messagebox.showwarning("Atención", "Escribe una tarea primero")

    def marcar_completada(self):
        """Marca o desmarca una tarea como completada"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:  # Si hay algo seleccionado
            indice = seleccion[0]
            tarea = self.lista_tareas.get(indice)

            # Cambiar el estilo si está completada
            if tarea.startswith("✓ "):
                tarea = tarea[2:]  # Quitar el check
            else:
                tarea = "✓ " + tarea  # Añadir el check

            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, tarea)
            self.actualizar_contador()

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:  # Si hay algo seleccionado
            self.lista_tareas.delete(seleccion[0])
            self.actualizar_contador()

    def actualizar_contador(self):
        """Actualiza el contador de tareas"""
        total = self.lista_tareas.size()
        completadas = sum(1 for i in range(total)
                          if self.lista_tareas.get(i).startswith("✓ "))
        self.contador.config(text=f"Tareas: {total} | Completadas: {completadas}")


# Iniciar la aplicación
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = GestorTareas(ventana_principal)
    ventana_principal.mainloop()