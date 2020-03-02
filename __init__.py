from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from logica import *

def limpiarCampos():
    txt_simbolos.configure(state='normal')
    txt_caracteres.configure(state='normal')
    txt_numeros.configure(state='normal')

    txt_simbolos.delete("1.0", END)
    txt_caracteres.delete("1.0", END)
    txt_numeros.delete("1.0", END)

    txt_simbolos.configure(state='disabled')
    txt_caracteres.configure(state='disabled')
    txt_numeros.configure(state='disabled')

def leerTexto():
    limpiarCampos()
    # capturar el texto ingresado por el usuario
    entrada = txt_entrada.get("1.0", END) # inicioFila.inicioColumna, finFila.finColumna o END para tomar todo el texto
    
    txt_simbolos.configure(state='normal')
    txt_simbolos.insert('end', capturarSimbolos(entrada))
    txt_simbolos.configure(state='disabled')

    txt_caracteres.configure(state='normal')
    txt_caracteres.insert('end', capturarCaracteres(entrada))
    txt_caracteres.configure(state='disabled')

    txt_numeros.configure(state='normal')
    txt_numeros.insert('end', capturarNumeros(entrada))
    txt_numeros.configure(state='disabled')

ventana = Tk()
#ventana.configure(background="#0FBFA3")
ventana.title("Analizador de Textos")

lbl_mensaje = Label(ventana, text="Ingrese el texto: ", font=("Arial Bold", 15))
#txt_entrada = Entry(ventana, width=10)
txt_entrada = scrolledtext.ScrolledText(ventana, width=40, height=5)
btn_leer = Button(ventana, text="Leer texto", command=leerTexto, bg="orange", fg="white")
lbl_mensaje_simbolos = Label(ventana, text="Símbolos: ", font=("Arial Bold", 13))
txt_simbolos = scrolledtext.ScrolledText(ventana, width=40, height=5)
lbl_mensaje_caracteres = Label(ventana, text="Caracteres: ", font=("Arial Bold", 13))
txt_caracteres = scrolledtext.ScrolledText(ventana, width=40, height=5)
lbl_mensaje_numeros = Label(ventana, text="Números: ", font=("Arial Bold", 13))
txt_numeros = scrolledtext.ScrolledText(ventana, width=40, height=5)

# agregar los componentes a la ventana
lbl_mensaje.grid(column=1, row=0)
txt_entrada.grid(column=1, row=1, padx=5, pady=5)
btn_leer.grid(column=1, row=10, padx=5, pady=5)

lbl_mensaje_simbolos.grid(column=0, row=12, padx=5, pady=5)
txt_simbolos.grid(column=0, row=13, padx=5, pady=5)

lbl_mensaje_caracteres.grid(column=1, row=12, padx=5, pady=5)
txt_caracteres.grid(column=1, row=13, padx=5, pady=5)

lbl_mensaje_numeros.grid(column=2, row=12, padx=5, pady=5)
txt_numeros.grid(column=2, row=13, padx=5, pady=5)

txt_simbolos.configure(state='disabled')
txt_caracteres.configure(state='disabled')
txt_numeros.configure(state='disabled')


txt_entrada.focus()
ventana.geometry("1100x350")                     # configurar el tamaño de la ventana (ancho * altura)
ventana.mainloop()                              # mostrar la ventana al usuario