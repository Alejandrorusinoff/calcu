importar tkinter como tk
desde tkinter import ttk
desde el cuadro de mensaje de importación de tkinter
del libro de trabajo de importación openpyxl
desde openpyxl import load_workbook
importar sistema operativo
solicitudes de importación
 
#########################
 
def guardar (orden):
	ws = wb.active
	ws.append (orden)
	wb.save (nombre de archivo = "empanadas.xlsx")
	f = abierto ("datostarde.csv", "a")
	f.write (orden [0] + "," + str (orden [1]) + "," + str (orden [2]) + "," + str (orden [3]) + "," + str (orden [4]) + "\ n")
	f.close ()
 
def validar (dato):
	si dato:
		tratar:
			dato = int (dato)
			volver dato
		excepto ValueError:
			volver -1
	más:
		volver -1
 
 
def borrar ():
	ccarne.delete (0, tk.END)
	cjyq.delete (0, tk.END)
	ch.delete (0, tk.END)
	ccliente.delete (0, tk.END)
 
 
def pedido ():
	cantc = ccarne.get ()
	cantc = validar (cantc)
	cantjyq = cjyq.get ()
	cantjyq = validar (cantjyq)
	canth = ch.get ()
	canth = validar (canth)
	cunit = costos ()
	si cantc> = 0 y cantjyq> = 0 y canth> = 0:
		cliente = ccliente.get ()
		si cliente:
			respuesta = messagebox.askyesno (title = "Pregunta", message = "¿Confirma el pedido?")
			si respuesta:
				costot = (cantc + cantjyq + canth) * cunit
				gustos = [cliente, cantc, cantjyq, canth, costot]
				#guardar
				guardar (gustos)
				messagebox.showinfo (título = "Información", mensaje = "Pedido Exitoso")
				borrar ()
			más:
				messagebox.showinfo (título = "Información", mensaje = "Pedido en pausa")
		más:
			messagebox.showwarning (title = "Advertencia", message = "Error, ingrese nombre del cliente")
	más:
		messagebox.showwarning (title = "Advertencia", message = "Error, ingrese datos correctos")
 
def cancelar_pedido ():
	respuesta = messagebox.askyesno (title = "Pregunta", message = "¿Desea cancelar el pedido?")
	si respuesta:
		ccarne.delete (0, tk.END)
		cjyq.delete (0, tk.END)
		ch.delete (0, tk.END)
		ccliente.delete (0, tk.END)
 
def comprobarArchivo ():
	existe = os.path.exists ("empanadas.xlsx")
	si existe:
		wb = load_workbook (nombre de archivo = "empanadas.xlsx")
		ws = wb.active
	más:
		wb = Libro de trabajo ()
		ws = wb.active
		titulo = ["Nombre", "Carne", "JYQ", "Humita", "Total"]
		ws.append (titulo)
		wb.save (nombre de archivo = "empanadas.xlsx")
		f = abierto ("datostarde.csv", "a")
		f.write ("Nombre, Carne, JYQ, Humita, Total \ n")
		f.close ()
	volver wb
 
def costos ():
	r = request.get ("https://www.dolarsi.com/api/api.php?type=cotizador")
	valor = r.json () [0] ["casa"] ["venta"]
	dolar = float (valor.replace (",", "."))
	costo = redondo (dolar / 10) * 10
	costo de retorno
 
#########################
 
wb = comprobarArchivo ()
 
#########################
 
ventana = tk.Tk ()
ventana.config (ancho = 400, alto = 400)
ventana.title ("Entrega")
 
##### etiquetas ######
ebienvenido = tk.Label (text = "------ Pedidos -------")
ebienvenido.place (x = 140, y = 20)
ecarne = tk.Label (text = "Ingrese cantidad de EC:")
ecarne.place (x = 50, y = 90)
ejyq = tk.Label (text = "Ingrese cantidad de JYQ:")
ejyq.place (x = 50, y = 150)
ejyq = tk.Label (text = "Ingrese cantidad de H:")
ejyq.place (x = 50, y = 210)
ecliente = tk.Label (text = "Nombre del cliente:")
ecliente.place (x = 50, y = 280)
 
 
 
##### cajas #########
ccarne = tk.Entry ()
ccarne.place (x = 230, y = 90)
cjyq = tk.Entry ()
cjyq.place (x = 230, y = 150)
ch = tk.Entry ()
ch.place (x = 230, y = 210)
ccliente = tk.Entry ()
ccliente.place (x = 230, y = 280)
 
##### Botones #########
 
bpedido = tk.Button (text = "Hacer Pedido", comando = pedido)
bpedido.place (x = 270, y = 330, alto = 40, ancho = 100)
 
bcancelar = tk.Button (text = "Cancelar Pedido", comando = cancelar_pedido)
bcancelar.place (x = 150, y = 330, altura = 40, ancho = 100)
 
bcancelar = tk.Button (texto = "Información")
bcancelar.place (x = 30, y = 330, altura = 40, ancho = 100)
 
 
ventana.mainloop ()
