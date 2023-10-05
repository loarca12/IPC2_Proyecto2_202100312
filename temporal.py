import tkinter as tk
from tkinter import messagebox

def guardar():
    texto = textbox.get()  # Obtiene el texto del TextBox
    with open("archivo.txt", "w") as archivo:
        archivo.write(texto)
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

ventana.mainloop()