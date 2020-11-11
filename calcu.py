importar tkinter como tk
desde tkinter import ttk
desde el cuadro de mensaje de importación de tkinter
importar sys
 
 
##############################
 
def convertir (dato):
	tratar:
		dato = int (dato)
		volver dato
	excepto ValueError:
		tratar:
			dato = flotar (dato)
			volver dato
		excepto ValueError:
			devolver "error"
 
 
def sumar ():
	cajar.delete (0, tk.END)
	a = cajauno.get ()
	b = cajados.get ()
	a = convertir (a)
	b = convertir (b)
	si a! = "error" yb! = "error":
		c = a + b
	más:
		c = "Error solo números"
	cajar.insert (0, c)
 
 
def restar ():
	cajar.delete (0, tk.END)
	a = cajauno.get ()
	b = cajados.get ()
	a = convertir (a)
	b = convertir (b)
	si a! = "error" yb! = "error":
		c = a - b
	más:
		c = "Error solo números"
	cajar.insert (0, c)
 
 
def multiplicar ():
	cajar.delete (0, tk.END)
	a = cajauno.get ()
	b = cajados.get ()
	a = convertir (a)
	b = convertir (b)
	si a! = "error" yb! = "error":
		c = a * b
	más:
		c = "Error solo números"
	cajar.insert (0, c)
 
 
def dividir ():
	cajar.delete (0, tk.END)
	a = cajauno.get ()
	b = cajados.get ()
	a = convertir (a)
	b = convertir (b)
	si a! = "error" yb! = "error":
		tratar:
			c = a / b
		excepto ZeroDivisionError:
			c = "Error de división por cero"
	más:
		c = "Error solo números"
	cajar.insert (0, c)
 
 
def salir ():
	respuesta = messagebox.askyesno (title = "Pregunta", message = "¿Desea salir?")
	si respuesta:
		sys.exit ()
 
def informar ():
	messagebox.showinfo (título = "V1.1", mensaje = "Calculadora Python")
 
##############################
 
ventana = tk.Tk ()
ventana.config (ancho = 300, alto = 300)
etq1 = tk.Label (text = "Dato 1:")
etq1.place (x = 20, y = 30)
etq2 = tk.Label (text = "Dato 2:")
etq2.place (x = 160, y = 30)
cajauno = tk.Entry ()
cajauno.place (x = 20, y = 60)
cajados = tk.Entry ()
cajados.place (x = 160, y = 60)
botones = tk.Button (texto = "+", comando = sumar)
botons.place (x = 25, y = 120, ancho = 50, alto = 30)
botonr = tk.Button (texto = "-", comando = restar)
botonr.place (x = 95, y = 120, ancho = 50, alto = 30)
botonm = tk.Button (texto = "x", comando = multiplicador)
botonm.place (x = 165, y = 120, ancho = 50, alto = 30)
botonm = tk.Button (texto = "/", comando = dividir)
botonm.place (x = 235, y = 120, ancho = 50, alto = 30)
etb = tk.Label (texto = "---- Botonera ----")
etb.place (x = 100, y = 90)
cajar = tk.Entry ()
cajar.place (x = 90, y = 200)
etr = tk.Label (text = "Resultado:")
etr.place (x = 90, y = 170)
botoni = tk.Button (texto = "Información", comando = informar)
botoni.place (x = 40, y = 250, ancho = 80, alto = 30)
botonsalir = tk.Button (text = "Salir", comando = salir)
botonsalir.place (x = 180, y = 250, ancho = 80, alto = 30)
ventana.mainloop ()