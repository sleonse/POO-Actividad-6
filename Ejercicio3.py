# Ejercicio 9.1 POO Actividad 6
import tkinter as tk
from tkinter import messagebox
class Contacto:
    def __init__(self, nombre, apellido, fecha, direccion, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class Interfaz:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Detalles de contacto")
        self.ventana_principal.geometry("600x350")
        
        self.frame_datos = tk.Frame(self.ventana_principal)
        self.frame_datos.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.label_nombres = tk.Label(self.frame_datos, text = 'Nombres:')
        self.label_nombres.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        
        self.entry_nombres = tk.Entry(self.frame_datos, width = 25)
        self.entry_nombres.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_apellidos = tk.Label(self.frame_datos, text = 'Apellidos:')
        self.label_apellidos.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')

        self.entry_apellidos = tk.Entry(self.frame_datos, width = 25)
        self.entry_apellidos.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_fecha = tk.Label(self.frame_datos, text = 'Fecha nacimiento:')
        self.label_fecha.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')

        self.entry_fecha = tk.Entry(self.frame_datos, width = 25)
        self.entry_fecha.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_direccion = tk.Label(self.frame_datos, text = 'Dirección:')
        self.label_direccion.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')

        self.entry_direccion = tk.Entry(self.frame_datos, width = 25)
        self.entry_direccion.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_telefono = tk.Label(self.frame_datos, text = 'Teléfono:')
        self.label_telefono.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'w')

        self.entry_telefono = tk.Entry(self.frame_datos, width = 25)
        self.entry_telefono.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_correo = tk.Label(self.frame_datos, text = 'Correo:')
        self.label_correo.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'w')

        self.entry_correo = tk.Entry(self.frame_datos, width = 25)
        self.entry_correo.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_agregar = tk.Button(self.frame_datos, text = 'Agregar', command = self.agregar_contacto)
        self.boton_agregar.grid(row = 6, column = 1, padx = 5, pady = 15, sticky = 'nsew')

        self.frame_lista = tk.Frame(self.ventana_principal)
        self.frame_lista.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.scrollbar_lista = tk.Scrollbar(self.frame_lista)
        self.scrollbar_lista.pack(side = tk.RIGHT, fill = tk.Y)

        self.lista_contactos = tk.Listbox(self.frame_lista, width = 40, height = 15, yscrollcommand = self.scrollbar_lista.set)
        self.lista_contactos.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
        self.scrollbar_lista.config(command = self.lista_contactos.yview)
        self.ventana_principal.mainloop()

    def agregar_contacto(self):
        nombre = self.entry_nombres.get()
        apellido = self.entry_apellidos.get()
        fecha = self.entry_fecha.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()


        if not nombre or not apellido or not fecha or not direccion or not telefono or not correo:
             messagebox.showerror("Error", "No se permiten campos vacios")
             return
        nuevo_contacto = Contacto(nombre, apellido, fecha, direccion, telefono, correo)

        contacto = f"{nombre}-{apellido}-{fecha}-{direccion}-{telefono}-{correo}"
        
        self.lista_contactos.insert(tk.END, contacto)

        self.entry_nombres.delete(0, 'end')
        self.entry_apellidos.delete(0, 'end')
        self.entry_fecha.delete(0, 'end')
        self.entry_direccion.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')
        self.entry_correo.delete(0, 'end')

Hola = Interfaz()