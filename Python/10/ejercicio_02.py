# Uso de librería TKinter, para crear una ventana
#   que contiene una lista

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Lista
lista = ['La Serena', 'Coquimbo', 'Vicuña']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=3, listvariable=lista_items)
listbox.grid(column=1, row=3, sticky=tkinter.W)

window.mainloop()
