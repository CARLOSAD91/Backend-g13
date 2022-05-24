
from tkinter import *
from tkinter import messagebox

def saludar():
  print('Hola mundo')
  messagebox.showinfo('mensaje', 'hola' + textNombre.get())
app = Tk()
app.title('Mi primera interfaz grafica')
app.geometry('400x400')
frame = LabelFrame(app, text='Ventana')
frame.grid(row=0, column=0, columnspan=3, pady=10, padx=20)
lbNombre = Label(frame, text='Nombre: ')
lbNombre.grid(row=1, column=0)
#caja de texto
textNombre = Entry(frame)
textNombre.grid(row=1, column=1)
#boton
btnSaludo = Button(frame, text='saludar', command=saludar)
btnSaludo.grid(row=1, column=2)

app.mainloop()