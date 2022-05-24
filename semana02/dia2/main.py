from multiprocessing import context
from flask import Flask, render_template,request
import requests

url = "https://api.github.com/users/CARLOSAD91"


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("tokenfirebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

@app.route('/')
def index():
  
  data =  requests.get(url)
  
  context = data.json()
  
  return render_template('home.html', **context)

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
  
  lsProyectos = []
  for doc in docProyectos:
    dicProyecto = doc.to_dict()
    lsProyectos.append(dicProyecto)
    
  context = {
    'proyectos': lsProyectos
  }
  
  return render_template('portafolio.html', **context)

@app.route('/contacto')
def contacto():
  return render_template('contacto.html')
  
  
app.run(debug=True, port=5000)