import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




def presionado():
    saludo.delete(0,tk.END)
    nombre = caja.get()
    if nombre:
        saludar = "hola " + nombre
        saludo.insert(0,saludar)
        caja.delete(0,tk.END) #borrar
        #print("contiene")
    else:
        messagebox.showwarning(title="ciudado",message="error faltan nombres")# sale un cuadro con advertencia
    #print("hola ",nombre)



ventana = tk.Tk()
ventana.title("App")
ventana.config(width=300,height=300)

boton = ttk.Button(text="hola",command=presionado)
boton.place(x=20,y=20)
caja = tk.Entry()
caja.place(x=20,y=100)
etiqueta=tk.Label(text="Nombre")
etiqueta.place(x=20,y=60)
saludo = tk.Entry()
saludo.place(x=20,y=200)



ventana.mainloop()