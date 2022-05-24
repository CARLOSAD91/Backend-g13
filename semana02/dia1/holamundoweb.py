from flask import Flask, render_template, request

#creamos objeto de la clase Flask
app = Flask(__name__)

#creamos mi primera ruta
@app.route('/')
def index():
  return '<center><h1>Hola mundo Flask</h1></center>'

@app.route('/saludo')
def saludo():
  nombre = request.args.get('nombre', 'no hay nombre')
  return '<center><h1><b>Hola {}</b></h1></center>'.format(nombre)

@app.route('/suma')
#desplegamos nuestra app web
def suma():
  n1 = request.args.get('n1', '0')
  n2 = request.args.get('n2', '0')
  resultado = int(n1) + int(n2)
  return '<center><b>la suma de {} + {} es {}</b></center>'.format(n1, n2, resultado)

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0, n2=0):
  resultado = n1-n2
  return '<center><b>la resta de {} - {} es {}</b></center>'.format(n1, n2, resultado)


app.run(debug=True)
  