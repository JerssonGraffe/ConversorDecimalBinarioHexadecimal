from tkinter import *
import tkinter as tk

main = Tk()
main.title("Conversor Decimal Binario Hexadecimal")
main.resizable(False,False)

#Funciones
def ConvDecimalBinario():

    texto = entrada.get()

    try:
        numeroDecimal = int(texto)
        binario = bin(numeroDecimal)[2:]
    except:
        binario = "Entrada no válida"

    salida.delete(1.0, tk.END)
    salida.insert(tk.END, binario)

def ConvDecimalHexaDecimal():

    texto = entrada.get()

    try:
        numeroDecimal = int(texto)
        hexa = hex(numeroDecimal)[2:]
    except:
        hexa = "Entrada no válida"

    salida.delete(1.0, tk.END)
    salida.insert(tk.END, hexa)



text = Label(text="Conversor Decimal a (Binario ou Hexadecimal)")
text.grid(row=0,column=0, padx=30,pady=15, columnspan= 2)


textEntrada = Label(text="Digite o numero a converter:")
textEntrada.grid(row=1,column=0, pady=15)
entrada = Entry(main)
entrada.grid(row=1,column=1,pady=15, columnspan= 2)

botonConvertir = Button(text= "Convertir a Binario", command=ConvDecimalBinario)
botonConvertir.grid(row=2,column=0, pady=10)

botonConvertir2 = Button(text= "Convertir a Hexadecimal", command=ConvDecimalHexaDecimal)
botonConvertir2.grid(row=2,column=1, pady=10)

salida = Text(main, height=5, width=20)
salida.grid(row=3,column=0, padx=30,pady=10, columnspan= 2)



main.mainloop()