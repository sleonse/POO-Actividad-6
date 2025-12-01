# Ejercicio 8.4 POO Actividad 6
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
class empleado:
    def __init__(self, nombre: str, apellido: str, cargo: str, genero: str, salario: int, dias_trabajados: int, otros: int, salud: int, pensiones: int):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.genero = genero
        self.salario = salario
        self.dias_trabajados = dias_trabajados
        self.otros = otros
        self.salud = salud
        self.pensiones = pensiones

    def calcular_nomina(self):
        nomina = (self.dias_trabajados * self.salario) + self.otros - self.salud - self.pensiones
        return nomina


class interfaz:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.geometry("400x200")
        self.ventana_principal.resizable(False, False)
        self.ventana_principal.columnconfigure(0, minsize = 100)

        self.empleados = []




        # Frame botones

        self.frame_botones_principales = tk.Frame(self.ventana_principal)
        
        self.label_menu = tk.Label(self.frame_botones_principales, text = 'Gestor de nominas')
        self.label_menu.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')



        self.boton_agregar_empleado = tk.Button(self.frame_botones_principales, text = 'Agregar empleado', command = self.abrir_agregar_empleado)
        self.boton_agregar_empleado.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_calcular_nomina = tk.Button(self.frame_botones_principales, text = 'Calcular nomina', command = self.abrir_calcular_nomina)
        self.boton_calcular_nomina.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_guardar_archivo = tk.Button(self.frame_botones_principales, text = 'Guardar archivo', command = self.guardar_archivo)
        self.boton_guardar_archivo.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.estado_archivo = tk.Label(self.frame_botones_principales, text = '', width=25)
        self.estado_archivo.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.frame_botones_principales.grid(row = 1, column = 1, padx = 5, pady = 5)






        self.ventana_principal.mainloop()

    def abrir_agregar_empleado(self):
        # Ventana de agregar empleado

        self.ventana_agregar_empleado = tk.Toplevel(self.ventana_principal)
        self.ventana_agregar_empleado.title("Agregar empleado")
        self.ventana_agregar_empleado.geometry("300x360")
        self.ventana_agregar_empleado.resizable(False, False)

        self.frame_agregar_empleado = tk.Frame(self.ventana_agregar_empleado)
        self.frame_agregar_empleado.columnconfigure(0, minsize = 120, weight = 1)
        self.frame_agregar_empleado.columnconfigure(1, minsize = 120, weight = 1)

        self.label_nombre = tk.Label(self.frame_agregar_empleado,text = 'Nombre:')
        self.label_nombre.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.entry_nombre = tk.Entry(self.frame_agregar_empleado)
        self.entry_nombre.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_apellidos = tk.Label(self.frame_agregar_empleado, text = 'Apellido:')
        self.label_apellidos.grid(row = 1, column = 0, padx = 5, pady = 5, sticky= 'nsew')

        self.entry_apellidos = tk.Entry(self.frame_agregar_empleado)
        self.entry_apellidos.grid(row = 1, column = 1, padx = 5, pady = 5, sticky= 'nsew')

        self.label_cargo = tk.Label(self.frame_agregar_empleado, text = 'Cargo:')
        self.label_cargo.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.lista_cargo = ttk.Combobox(self.frame_agregar_empleado, values = ['Directivo', 'Empleado'], state = 'readonly')
        self.lista_cargo.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.label_genero = tk.Label(self.frame_agregar_empleado, text = 'Genero:')
        self.label_genero.grid(row = 3, column = 0, padx = 5, pady = 5)

        self.lista_genero = ttk.Combobox(self.frame_agregar_empleado, values = ['Hombre', 'Mujer'], state = 'readonly')
        self.lista_genero.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.label_salario = tk.Label(self.frame_agregar_empleado, text = 'Salario por dia:')
        self.label_salario.grid(row = 4, column = 0, padx = 5, pady = 5, sticky= 'nsew')

        self.entry_salario = tk.Entry(self.frame_agregar_empleado)
        self.entry_salario.grid(row = 4, column = 1, padx = 5, pady = 5, sticky= 'nsew')

        self.label_dias_trabajados = tk.Label(self.frame_agregar_empleado, text = 'Dias trabajados:')
        self.label_dias_trabajados.grid(row = 5, column = 0, padx = 5, pady = 5)

        self.lista_dias = ttk.Combobox(self.frame_agregar_empleado, values = [i for i in range(0,31)], state = 'readonly')
        self.lista_dias.grid(row = 5, column = 1, padx = 5, pady = 5)

        self.label_otros = tk.Label(self.frame_agregar_empleado, text = 'Otros ingresos:')
        self.label_otros.grid(row = 6, column = 0, padx = 5, pady = 5, sticky= 'nsew')

        self.entry_otros = tk.Entry(self.frame_agregar_empleado)
        self.entry_otros.grid(row = 6, column = 1, padx = 5, pady = 5, sticky= 'nsew')

        self.label_salud = tk.Label(self.frame_agregar_empleado, text = 'Pagos por salud:')
        self.label_salud.grid(row = 7, column = 0, padx = 5, pady = 5, sticky= 'nsew')

        self.entry_salud = tk.Entry(self.frame_agregar_empleado)
        self.entry_salud.grid(row = 7, column = 1, padx = 5, pady = 5, sticky= 'nsew')

        self.label_pensiones = tk.Label(self.frame_agregar_empleado, text = 'Aporte pensiones:')
        self.label_pensiones.grid(row = 8, column = 0, padx = 5, pady = 5, sticky= 'nsew')

        self.entry_pensiones = tk.Entry(self.frame_agregar_empleado)
        self.entry_pensiones.grid(row = 8, column = 1, padx = 5, pady = 5, sticky= 'nsew')

        self.boton_agregar = tk.Button(self.frame_agregar_empleado, text = 'Agregar', command = self.agregar)
        self.boton_agregar.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = 'nsew')

        self.boton_borrar = tk.Button(self.frame_agregar_empleado, text = 'Borrar', command = self.borrar)
        self.boton_borrar.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = 'nsew')

        self.label_error = tk.Label(self.frame_agregar_empleado, text = '')
        self.label_error.grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2)


        self.frame_agregar_empleado.grid(row = 0, column = 0, padx = 5, pady = 5)

    def agregar(self):
        try:
            empleado_a_almacenar = empleado(self.entry_nombre.get(), self.entry_apellidos.get(), self.lista_cargo.get(), self.lista_genero.get(), int(self.entry_salario.get()), int(self.lista_dias.get()), int(self.entry_otros.get()), int(self.entry_salud.get()), int(self.entry_pensiones.get()))
            self.empleados.append(empleado_a_almacenar)
            self.entry_nombre.delete(0, tk.END)
            self.entry_apellidos.delete(0, tk.END)
            self.lista_cargo.set("")
            self.lista_genero.set("")
            self.entry_salario.delete(0, tk.END)
            self.lista_dias.set("")
            self.entry_otros.delete(0, tk.END)
            self.entry_salud.delete(0, tk.END)
            self.entry_pensiones.delete(0, tk.END)
            self.label_error.config(text = 'Empleado agregado exitosamente')
        except Exception as e:
            self.label_error.config(text = 'Error: ingrese datos validos')



    def borrar(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.lista_cargo.set("")
        self.lista_genero.set("")
        self.entry_salario.delete(0, tk.END)
        self.lista_dias.set("")
        self.entry_otros.delete(0, tk.END)
        self.entry_salud.delete(0, tk.END)
        self.entry_pensiones.delete(0, tk.END)

    def abrir_calcular_nomina(self):
        self.ventana_calcular_nomina = tk.Toplevel(self.ventana_principal)
        self.ventana_calcular_nomina.title("Calcular nomina")
        self.ventana_calcular_nomina.geometry("612x360")
        self.ventana_calcular_nomina.resizable(False, False)
        


        self.frame_calcular_nomina = tk.Frame(self.ventana_calcular_nomina)
        self.label_tabla_nominas = tk.Label(self.frame_calcular_nomina, text = 'Tabla de nominas')
        self.label_tabla_nominas.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nsew', columnspan = 2)
        self.tabla_nominas = ttk.Treeview(self.frame_calcular_nomina, columns = ('Nombre', 'Apellido','Salario mensual'), show='headings')
        self.tabla_nominas.heading('Nombre', text='Nombre')
        self.tabla_nominas.heading('Apellido', text='Apellidos')
        self.tabla_nominas.heading('Salario mensual', text='Sueldo Mensual')


        self.total_nominas = 0
        for empleado in self.empleados:
            sueldo = empleado.calcular_nomina()
            self.total_nominas += sueldo
            self.tabla_nominas.insert('',tk.END, values =(empleado.nombre, empleado.apellido, f'${sueldo}'))

        self.tabla_nominas.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)
        self.total_tabla = tk.Label(self.frame_calcular_nomina, text = f'Total: ${self.total_nominas}')
        self.total_tabla.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)

        self.frame_calcular_nomina.grid(row = 1, column = 0, columnspan = 2)

    def guardar_archivo(self):
        carpeta = filedialog.askdirectory(title="Seleccione carpeta para guardar")
        if carpeta:
            ruta_completa = f'{carpeta}/nominas.txt'
            try:
                with open(ruta_completa, 'w') as archivo:
                    archivo.write('Reporte de nominas\n')
                    for empleado in self.empleados:
                        archivo.write(f'Nombre: {empleado.nombre}\n')
                        archivo.write(f'Apellido: {empleado.apellido}\n')
                        archivo.write(f'Cargo: {empleado.cargo}\n')
                        archivo.write(f'Genero: {empleado.genero}\n')
                        archivo.write(f'Salario por dia: {empleado.salario}\n')
                        archivo.write(f'Dias trabajados al mes: {empleado.dias_trabajados}\n')
                        archivo.write(f'Otros ingresos: {empleado.otros}\n')
                        archivo.write(f'Pagos por salud: {empleado.salud}\n')
                        archivo.write(f'Aporte pension: {empleado.pensiones}\n')
                        archivo.write(f'Total: {empleado.calcular_nomina()}\n')
                        archivo.write(f'\n')
                    self.estado_archivo.config(text = 'Archivo guardado exitosamente')
            except:
                self.estado_archivo.config(text = 'Error al guardar el archivo')            



Hola = interfaz()

