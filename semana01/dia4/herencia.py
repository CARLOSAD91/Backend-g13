class Persona:
  
  def __init__(self, nom,ema):
    
    self.nombre = nom
    self.email = ema
    
  def mostrar(self):
    print('Nombre: '+ self.nombre + 'email: ' + self.email)

class Alumno(Persona):
  pass
  
 
    
class Profesor(Persona) :
  
  def __init__(self, nom, ema, mod):
    super().__init__(nom, ema)
    self.modulo = mod
    
  def mostrar(self):
      super().mostrar()
      print('dicata el modulo: ', self.modulo)
 

alu1 = Alumno('carlos tellos', 'ctello@correo.com')
alu1.mostrar()

profe1 = Profesor('cesar mayta', 'cesar@gmail.com','backend')
profe1.mostrar()

