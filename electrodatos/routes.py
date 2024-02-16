from electrodatos import app
from electrodatos.models import Electrodata
from flask import render_template

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

@app.route("/datos-ejemplo/<int:id_cliente>")
def datos_ejemplo(id_cliente):
    electrodatos = Electrodata("electrodatos/datos/electrodatos.csv")
    series = electrodatos.cliente(id_cliente)
    cadena = f"var fechas = {series[0]};\nvar etiquetas = {series[1]};"
    return cadena

@app.route("/grafico")
def grafico():
    return render_template("graphjs.html")