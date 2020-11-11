import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

def salir():
    respuesta=messagebox.askyesno(title="pregunta",message="¿desea salir?")
    if respuesta:
        sys.exit()

def convertir(dato):
    try:
        dato=int(dato)
        return dato
    except ValueError:
        try:
            dato=float(dato)
            return dato
        except ValueError:
            return "error"

def sumar():
    a=cajauno.get()
    b=cajados.get()
    a=convertir(a)
    b=convertir(b)
    if a != "error" and b !="error":
        c=a+b
    else:
        c = "error solo numeros"
    cajar.insert(0,c)






ventana = tk.Tk()
ventana.title("App")
ventana.config(width=300,height=300)

etq1=tk.Label(text="dato 1:")
etq1.place(x=20,y=30)

etq2=tk.Label(text="dato 2:")
etq2.place(x=160,y=30)
cajauno=tk.Entry()
cajauno.place(x=20,y=60)
cajados=tk.Entry()
cajados.place(x=150,y=60)

botons=tk.Button(text="+",command=sumar())
botons.place(x=20,y=120,width=50,height=30)

botonr=tk.Button(text="-")
botonr.place(x=100,y=120,width=50,height=30)
botonm=tk.Button(text="x")
botonm.place(x=180,y=120,width=50,height=30)

botond=tk.Button(text="/")
botond.place(x=240,y=120,width=50,height=30)

etb=tk.Label(text="botonera")
etb.place(x=150,y=90)

cajar=tk.Entry()
cajar.place(x=90,y=200)
etr=tk.Label(text="resultados:")
etr.place(x=90,y=170)

botoni=tk.Button(text="info")
botoni.place(x=40,y=250,width=80,height=30)

botonsalir=tk.Button(text="salir", command=salir)
botonsalir.place(x=180,y=250,width=80,height=30)




ventana.mainloop()