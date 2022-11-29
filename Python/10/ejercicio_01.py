# Uso de librería TKinter, para crear una ventana
#   que contiene Radio Button, el cual se puede reiniciar su valor

import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Tarea N°1 GUI")

def reset():
    return selected.set(3)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='0', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='1', variable=selected)

bot = tkinter.Button(window, text="Reinicio", command=reset)
bot2 = tkinter.Button(window, text="Salir", command=window.destroy)

r1.pack()
r2.pack()
bot.pack()
bot2.pack()

window.mainloop()
