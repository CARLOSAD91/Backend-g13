import email
from tkinter import  *
from tkinter import messagebox
from turtle import bgcolor
from tkinter.ttk import Treeview

class Alumnos:
  
  def registrarAlumno(self):
    self.TrvAlumnos.insert('',0,text= self.nombre.get(), values= self.email.get())
  
  def __init__(self, window):
    self.wind = window
    self.wind.title('CRUD DE ALUMNOS')
    self.wind.geometry('420x390')
    self.wind.configure(bg = '#49a')
    
    #frame
    
    frame = LabelFrame(self.wind, text='Registro de nuevo Alumno')
    frame.grid(row=0, column=0, columnspan=2, pady=10)
    
    #LABEL NOMBRE
    lbNombre = Label(frame, text='Nombre: ')
    lbNombre.grid(row=1, column=0)
    
    #text nombre
    self.nombre = Entry(frame)
    self.nombre.grid(row=1, column=1)
    
     #LABEL EMAIL
    lbEmail = Label(frame, text='Email: ')
    lbEmail.grid(row=2, column=0)
    
    #text nombre
    self.email = Entry(frame)
    self.email.grid(row=2, column=1)
    
    ########## BOTON NUEVO ALUMNO ########
    btnNuevoAlumno = Button(frame, text='Registrar', command=self.registrarAlumno)
    btnNuevoAlumno.grid(row=4, columnspan=2, sticky=W + E)
    
    ######### TREEVIEW #############
    self.TrvAlumnos = Treeview(height=10, columns=2)
    self.TrvAlumnos.grid(row=5, column=0, columnspan=2, padx=10)
    self.TrvAlumnos.heading('#0', text='Nombre', anchor=CENTER)
    self.TrvAlumnos.heading('#1', text='Email', anchor=CENTER)
  
    
window = Tk()
app = Alumnos(window)
window.mainloop()