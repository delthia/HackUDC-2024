from electrodatos import app
from electrodatos.models import Electrodata
from flask import render_template
import datetime

@app.route("/")
def homepage():
    return "Hola, mundo"

@app.route("/clientes")
def clients():
    return "Clients"

@app.route("/cliente/<int:id_cliente>")
def cliente(id_cliente):
    ids_clientes = list(range(1, 100))
    if id_cliente not in ids_clientes:
        return "Parece que no eres un cliente que exista"
    return f"Eres el cliente {id_cliente}"

@app.route("/datos-ejemplo/<int:id_cliente>/<inicio>/<fin>")
def datos_ejemplo(id_cliente, inicio, fin):
    electrodatos = Electrodata("electrodatos/datos/electrodatos.csv")
    inicio, fin = inicio.split('-'), fin.split('-')
    series = electrodatos.cliente(id_cliente, datetime.datetime(int(inicio[0]), int(inicio[1]), int(inicio[2])), datetime.datetime(int(fin[0]), int(fin[1]), int(fin[2])))
    cadena = f"var fechas = {series[0]};\nvar datos = {series[1]};"
    return cadena

@app.route("/grafico")
def grafico():
    return render_template("graphjs.html")
