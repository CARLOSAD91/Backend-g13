from multiprocessing import context
from flask import Flask, render_template,request, session
#import requests

#url = "https://api.github.com/users/CARLOSAD91"

import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

## para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()


app = Flask(__name__)
# crearmos una clave secreta para la sesion
app.secret_key = 'qwerty12345'

@app.route('/')
def index():
  
  colBiografia = db.collection('biografia')
  docBiografia = colBiografia.get()
  
  colEnlaces = db.collection('enlaces')
  docEnlaces = colEnlaces.get()
  
  lstEnalces = []
  for doc in docEnlaces:
    dicEnlaces = doc.to_dict()
    lstEnalces.append(dicEnlaces)

  
  for doc in docBiografia:
    dicBiografia = doc.to_dict()
    
    
  session['biografia'] = dicBiografia
  session['enlaces'] = lstEnalces
  
  
  #data =  requests.get(url)
  #context = data.json()
  
  return render_template('home.html')

@app.route('/peliculas')
def peliculas():
  listaPeliculas = ['Spiderman', 'Batman', 'Superman', 'Ironman']
  nombre = request.args.get('nombre','no hay nombre')
  context = {
    nombre:nombre,
    'peliculas': listaPeliculas
  }
  
  return render_template('peliculas.html', **context)

######################## RUTAS DE MI PAGINA ##############################
@app.route('/acercade')
def about():
       
  return render_template('acercade.html')


@app.route('/portafolio')
def portafolio():
  
  colProyectos = db.collection('proyectos')
  docProyectos = colProyectos.get()
  
  ltsProyectos = []
  for doc in docProyectos:
    print(doc.to_dict())
    dicProyecto = doc.to_dict()
    ltsProyectos.append(dicProyecto)
    
  context = {
    'proyectos': ltsProyectos
  }
      
  return render_template('portafolio.html', **context)

@app.route('/contacto')
def contacto():
  
  return render_template('contacto.html')
  
  
app.run(debug=True, port=5000)