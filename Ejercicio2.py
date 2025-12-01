# Ejercicio 8.5 POO Actividad 6
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class Habitacion:
    def __init__(self, numero, ocupada, fecha, nombre, apellidos, documento):
        self.numero = numero
        self.ocupada = ocupada
        self.fecha = fecha
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento = documento



class Hotel:
    def __init__(self):
        self.habitaciones = []
        for i in range(1,11):
            hab = Habitacion(i, False, None, None, None, None)
            self.habitaciones.append(hab)




class Interfaz:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.geometry("380x200")
        self.ventana_principal.resizable(False, False)
        self.ventana_principal.columnconfigure(0, minsize = 100)

        self.frame_botones_menu = tk.Frame(self.ventana_principal)
        
        self.label_menu = tk.Label(self.frame_botones_menu, text = 'Hotel')
        self.label_menu.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')



        self.boton_consultar_hab = tk.Button(self.frame_botones_menu, text = 'Consultar habitaciones', command = self.abrir_habitaciones)
        self.boton_consultar_hab.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_salida_huespedes = tk.Button(self.frame_botones_menu, text = 'Salida de huespedes', command = self.abrir_salida_huespedes)
        self.boton_salida_huespedes.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.frame_botones_menu.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.ocupadas = []
        self.hotel = Hotel()

        self.ventana_principal.mainloop()

    def abrir_habitaciones(self):
        self.ventana_habitaciones = tk.Toplevel(self.ventana_principal)
        self.ventana_habitaciones.geometry('780x300')
        self.ventana_habitaciones.resizable(False, False)
        self.ventana_habitaciones.title("Habitaciones")
        self.frame_habitaciones = tk.Frame(self.ventana_habitaciones)
        self.label_estado_habitaciones = []
        for i in range(0,7,3):
            self.frame_habitaciones.rowconfigure(i, minsize = 40)
        for i in range(1,9,2):
            self.frame_habitaciones.columnconfigure(i, minsize = 40)
        for i in range(10): 
            if self.hotel.habitaciones[i].ocupada:
                estado = 'No disponible'
            else:
                estado = 'Disponible'
            label_habitacion = tk.Label(self.frame_habitaciones, text = f'Habitacion {i+1}')
            label_estado = tk.Label(self.frame_habitaciones, text = estado, width=15)
            fila = 1 if i < 5 else 4
            columna = 2*i if i < 5 else 2*(i -5)
            label_habitacion.grid(row = fila, column = columna, padx = 5, pady = 5, sticky = 'nsew')
            label_estado.grid(row = fila + 1, column = columna, padx = 5, pady = 5, sticky = 'nsew')
            self.label_estado_habitaciones.append(label_estado)
        self.frame_habitaciones.grid(row = 0, column = 0)


        self.frame_reserva = tk.Frame(self.ventana_habitaciones)
        self.frame_reserva.columnconfigure(2, minsize = 40)
        self.label_hab_reservar = tk.Label(self.frame_reserva, text = 'Habitacion a reservar:')
        self.label_hab_reservar.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.lista_hab = ttk.Combobox(self.frame_reserva, values = [hab.numero for hab in self.hotel.habitaciones if not hab.ocupada], state = 'readonly')
        self.lista_hab.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nsew')



        self.boton_aceptar = tk.Button(self.frame_reserva, text = 'Aceptar', width=20, command = self.ingreso)
        self.boton_aceptar.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = 'nsew')

        self.label_estado_num_hab = tk.Label(self.frame_reserva, text = '')
        self.label_estado_num_hab.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = 'nsew')

        self.frame_reserva.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2)


    def ingreso(self):
        if not self.lista_hab.get():
            return
        num_hab = int(self.lista_hab.get())
        if num_hab and self.hotel.habitaciones[int(self.lista_hab.get())-1].ocupada is False:
            self.ventana_ingreso =  tk.Toplevel(self.ventana_habitaciones)
            self.ventana_ingreso.geometry('300x270')
            self.ventana_ingreso.resizable(False, False)
            self.ventana_ingreso.title("Ingreso")

            self.frame_ingreso = tk.Frame(self.ventana_ingreso)
            self.frame_ingreso.columnconfigure(0, minsize = 10)
            self.frame_ingreso.columnconfigure(3, minsize = 10)

            self.label_num_habitacion = tk.Label(self.frame_ingreso, text = f'Habitacion: {num_hab}')
            self.label_num_habitacion.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.label_fecha = tk.Label(self.frame_ingreso, text = 'Fecha (aaaa-mm-dd):')
            self.label_fecha.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.entry_fecha = tk.Entry(self.frame_ingreso)
            self.entry_fecha.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'nsew')

            self.label_huesped = tk.Label(self.frame_ingreso, text = 'Huesped')
            self.label_huesped.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.label_nombre = tk.Label(self.frame_ingreso, text = 'Nombre:')
            self.label_nombre.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.entry_nombre = tk.Entry(self.frame_ingreso)
            self.entry_nombre.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = 'nsew')

            self.label_apellido = tk.Label(self.frame_ingreso, text = 'Apellidos:')
            self.label_apellido.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.entry_apellido = tk.Entry(self.frame_ingreso)
            self.entry_apellido.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = 'nsew')

            self.label_documento = tk.Label(self.frame_ingreso, text = 'Documento:')
            self.label_documento.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.entry_documento = tk.Entry(self.frame_ingreso)
            self.entry_documento.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = 'nsew')

            self.boton_aceptar_ingreso = tk.Button(self.frame_ingreso, text = 'Aceptar', command = self.reserva)
            self.boton_aceptar_ingreso.grid(row = 6, column = 1, padx = 5, pady = 5, sticky = 'nsew')

            self.boton_cancelar_ingreso = tk.Button(self.frame_ingreso, text = 'Cancelar', command=self.ventana_ingreso.destroy)
            self.boton_cancelar_ingreso.grid(row = 6, column = 2, padx = 5, pady = 5, sticky = 'nsew')

            self.frame_ingreso_estado = tk.Label(self.frame_ingreso, text = '')
            self.frame_ingreso_estado.grid(row = 7, column = 1, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2 )
            self.frame_ingreso.grid(row = 0, column = 0)


        else:
            self.label_estado_num_hab.config(text = 'Error: Habitacion no disponible')
            return

    def reserva(self):
        try:
            num_hab = int(self.lista_hab.get()) - 1
            datetime.strptime(self.entry_fecha.get(), '%Y-%m-%d')
            if self.entry_fecha.get() and self.entry_nombre.get() and self.entry_apellido.get() and self.entry_documento.get():
                self.hotel.habitaciones[num_hab].ocupada, self.hotel.habitaciones[num_hab].fecha = True, datetime.strptime(self.entry_fecha.get(), '%Y-%m-%d')
                self.hotel.habitaciones[num_hab].nombre, self.hotel.habitaciones[num_hab].apellidos, self.hotel.habitaciones[num_hab].documento = self.entry_nombre.get(), self.entry_apellido.get(), self.entry_documento.get()
                self.label_estado_habitaciones[num_hab].config(text = 'No disponible')
                self.ventana_ingreso.destroy()
                messagebox.showinfo("Éxito", "Reserva exitosa")

            else:
                self.frame_ingreso_estado.config(text = 'Error: Ingrese datos validos')
        except Exception as e:
            self.frame_ingreso_estado.config(text = f'Error: Ingrese datos validos')





    def abrir_salida_huespedes(self):

        self.seleccionar_salida_huesped = tk.Toplevel(self.ventana_principal)
        self.seleccionar_salida_huesped.geometry('200x150')
        self.seleccionar_salida_huesped.resizable(False, False)
        self.seleccionar_salida_huesped.title("Salida de huespedes")

        self.frame_seleccionar_huesped = tk.Frame(self.seleccionar_salida_huesped)
        self.label_seleccionar_hab = tk.Label(self.frame_seleccionar_huesped, text = 'Seleccione numero de habitacion')
        self.label_seleccionar_hab.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2)

        self.seleccion_huesped_salida = ttk.Combobox(self.frame_seleccionar_huesped, values = [hab.numero for hab in self.hotel.habitaciones if hab.ocupada], state = 'readonly')
        self.seleccion_huesped_salida.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2)

        self.boton_aceptar_salida = tk.Button(self.frame_seleccionar_huesped, text = 'Aceptar', command = self.aceptar_salida)
        self.boton_aceptar_salida.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_cancelar_salida = tk.Button(self.frame_seleccionar_huesped, text = 'Rechazar', command = self.seleccionar_salida_huesped.destroy)
        self.boton_cancelar_salida.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nsew' )

        self.estado_salida = tk.Label(self.frame_seleccionar_huesped, text = '')
        self.estado_salida.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nsew')
        self.frame_seleccionar_huesped.grid(row = 0, column = 0, columnspan = 3, rowspan = 3 , sticky = 'nsew')

    def aceptar_salida(self):
        if not self.seleccion_huesped_salida.get():
            self.estado_salida.config(text = 'Error: seleccione una habitacion')
            return
        hab = int(self.seleccion_huesped_salida.get()) - 1
        self.seleccionar_salida_huesped.destroy()
        self.ventana_salida_huesped = tk.Toplevel(self.ventana_principal)
        self.ventana_salida_huesped.geometry("235x400")
        self.ventana_salida_huesped.resizable(False, False)
        self.ventana_salida_huesped.title("Salida de huesped")

        self.frame_salida = tk.Frame(self.ventana_salida_huesped)
        self.frame_salida.columnconfigure(0, minsize = 10)
        self.frame_salida.columnconfigure(2, minsize = 10)

        self.label_sel_habitacion = tk.Label(self.frame_salida, text = f'Habitacion: {hab + 1}')
        self.label_sel_habitacion.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'w')

        self.label_fecha_ing = tk.Label(self.frame_salida, text = f'Fecha de ingreso: {self.hotel.habitaciones[hab].fecha.date()}')
        self.label_fecha_ing.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')

        self.label_fecha_sal = tk.Label(self.frame_salida, text = f'Fecha de salida: (aaaa-mm-dd):')
        self.label_fecha_sal.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')

        self.entry_fecha_sal = tk.Entry(self.frame_salida)
        self.entry_fecha_sal.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_calcular = tk.Button(self.frame_salida, text = 'Calcular', command=lambda: self.calcular(hab))
        self.boton_calcular.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'nsew')
    
        self.label_cantidad = tk.Label(self.frame_salida, text = 'Cantidad de dias:')
        self.label_cantidad.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = 'w')

        self.label_total = tk.Label(self.frame_salida, text = 'Total: $')
        self.label_total.grid(row = 6, column = 1, padx = 5, pady = 5, sticky = 'w')

        self.boton_registrar_salida = tk.Button(self.frame_salida, text = 'Registrar salida', state='disabled', command=lambda: self.registrar_salida(hab))
        self.boton_registrar_salida.grid(row = 7, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.frame_salida.grid(row = 0, column = 0, columnspan = 3, rowspan = 3, sticky = 'nsew')
    def calcular(self, hab):
        try:
            fecha_ingreso = self.hotel.habitaciones[hab].fecha

            fecha_salida = datetime.strptime(self.entry_fecha_sal.get(), '%Y-%m-%d')
            dias = (fecha_salida - fecha_ingreso).days
            if dias <= 0:
                self.label_cantidad.config(text = 'Cantidad de dias: Error')
                return
            self.label_cantidad.config(text = f'Cantidad de dias: {dias}')

            if hab < 5:
                valor_dia = 120000
            else:
                valor_dia = 160000
            total = dias * valor_dia
            self.label_total.config(text=f"Total: ${total:,}")
            self.boton_registrar_salida.config( state = 'normal' )
        except:
            self.label_cantidad.config(text = 'Cantidad de dias: Error')
            self.boton_registrar_salida.config(state='disabled')        
    def registrar_salida(self, hab):
        self.hotel.habitaciones[hab].ocupada, self.hotel.habitaciones[hab].fecha = False, None
        self.hotel.habitaciones[hab].nombre, self.hotel.habitaciones[hab].apellidos, self.hotel.habitaciones[hab].documento = None, None, None
        self.label_estado_habitaciones[hab].config(text = 'Disponible')
        messagebox.showinfo("Éxito", "Salida exitosa")
        self.ventana_salida_huesped.destroy()
Hola = Interfaz()