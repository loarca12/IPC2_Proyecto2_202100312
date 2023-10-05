import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import webbrowser
from graphviz import Digraph
import xml.etree.ElementTree as ET
from lectura import *


def inicializar():
    print("hola")

def cargar_archivo():
    filename = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    print(filename)
    if filename:
        with open(filename, 'r') as file:
            content = file.read()
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, "Archivo XML a analizar:\n\n" + content)
        messagebox.showinfo("Analizando archivo", "El archivo XML está siendo analizado...")

        lecXml.lectura(filename)
        data = "Datos extraídos del archivo XML..."
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, data)

def generar_archivo_xml():
    filename = filedialog.asksaveasfilename(defaultextension=".xml")
    if filename:
        # Crear el elemento raíz
        root = ET.Element("drones")

        # Crear un subelemento para un sistema de drones
        drone_system = ET.SubElement(root, "drone_system")
        drone_system.set("name", "Drone System 1")

        # Crear subelementos para las instrucciones
        instruction1 = ET.SubElement(drone_system, "instruction")
        instruction1.text = "Instrucción 1"
        instruction2 = ET.SubElement(drone_system, "instruction")
        instruction2.text = "Instrucción 2"

        # Crear un subelemento para el tiempo óptimo
        optimal_time = ET.SubElement(drone_system, "optimal_time")
        optimal_time.text = "Tiempo óptimo"

        # Crear un objeto ElementTree y escribir el XML a un archivo
        tree = ET.ElementTree(root)
        tree.write(filename)

def gestion_drones():
    x1 = listaPrincipal.mostrar()
    messagebox.showinfo("Mensaje", x1)

def gestion_sistemas():
    lecXml.grafica_sistemas()

def agregar_drones():
    
    def guardar():
        texto = textbox.get()  # Obtiene el texto del TextBox
        print(texto)
        b = dronesPrincipales(texto)
        listaPrincipal.agregar_al_final(b)
        listaPrincipal.ordenamiento_seleccion()
        messagebox.showinfo("Guardado", "El texto ha sido guardado correctamente.")

    def regresar():
        ventana.destroy()

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Cuadro de Texto")

    # Crear un TextBox
    textbox = tk.Entry(ventana, width=40)
    textbox.pack(padx=10, pady=10)

    # Crear el botón "Guardar"
    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar)
    boton_guardar.pack(pady=5)

    # Crear el botón "Regresar"
    boton_regresar = tk.Button(ventana, text="Regresar", command=regresar)
    boton_regresar.pack(pady=5)
        

    def regresar():
        text_widget.delete("1.0", tk.END)

def ver_listado_mensajes():
    pass

def seleccionar_mensaje():
    pass

def mostrar_instrucciones():
    pass

def ver_instrucciones_graficas():
    dot = Digraph()

    dot.node('A', 'Mensaje 1')
    dot.node('B', 'Mensaje 2')
    dot.node('C', 'Mensaje 3')
    dot.edges(['AB', 'AC'])

    dot.render('output.gv', view=True, format='png')


def ayuda_usuario():
    messagebox.showinfo("Ayuda", "GIANCARLO ADONAY CIFUENTES LOARCA\n202100312\nINTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 / SECCION N\nhttps://github.com/loarca12/IPC2_Proyecto2_202100312")

def salir_programa():
    root.quit()

root = tk.Tk()
root.title("Sistema de Gestion de vuelo de Drones")

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Inicializar sistema", command=inicializar)
file_menu.add_command(label="Cargar archivo XML", command=cargar_archivo)
file_menu.add_command(label="Generar archivo XML de salida", command=generar_archivo_xml)

drone_menu = tk.Menu(menu)
menu.add_cascade(label="Drones", menu=drone_menu)
drone_submenu = tk.Menu(drone_menu)
drone_menu.add_cascade(label="Gestion de Drones", menu = drone_submenu )
drone_submenu.add_command(label="Ver listado de drones", command=gestion_drones)
drone_submenu.add_command(label="Ver listado de sistemas", command=gestion_sistemas)
drone_submenu.add_command(label="Agregar nuevo Dron", command=agregar_drones)



message_menu = tk.Menu(menu)
menu.add_cascade(label="Mensajes", menu=message_menu)
message_submenu = tk.Menu(message_menu)
message_menu.add_cascade(label="Gestion de Mensajes", menu=message_submenu)
message_submenu.add_command(label="Ver listado de mensajes y sus instrucciones", command=ver_listado_mensajes)
message_submenu.add_command(label="Seleccionar un mensaje", command=seleccionar_mensaje)
message_submenu.add_command(label="Mostrar instrucciones para enviar un mensaje", command=mostrar_instrucciones)
message_submenu.add_command(label="Ver instrucciones gráficas", command=ver_instrucciones_graficas)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Ayuda", menu=help_menu)
help_menu.add_command(label="Ayuda de soporte Tecnico para el usuario", command=ayuda_usuario)

exit_menu = tk.Menu(menu)
menu.add_cascade(label="Salir", menu=exit_menu)
exit_menu.add_command(label="Salir del programa de Drones", command=salir_programa)

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack(expand=True, fill='both')

root.mainloop()


