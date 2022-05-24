#crear clase
class Automovil:
  #crear atributos
  def __init__(self, aa, pl,col, mar):
    self.año = aa
    self.placa = pl
    self.color = col 
    self.marca = mar
  
  def encender(self):
    print('encender' + self.marca)
    
  def avanzar(self):
    print('avanzar' + self.marca)
    
  def acelerar(self):
    print('acelerar' + self.marca)
    
  def frenar(self):
    print('frenar', self.marca)
    
#creacion de objetos
vw = Automovil(1970,'CH-1234', 'Amarillo', 'Volswvage')
print('se creo el objeto vw con los datos:')
print('año' + str(vw.año))
print('color' + vw.color)
print('placa' + vw.placa)
vw.encender()

tico = Automovil(1985, 'E3-2345', 'Rojo', 'Tico')
tico.encender()
tico.frenar()