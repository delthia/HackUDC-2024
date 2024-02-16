from electrodatos import app
from electrodatos.models import Electrodata
from flask import render_template, request
from datetime import datetime

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
    return render_template("cliente.html", cliente = id_cliente)
    return f"Eres el cliente {id_cliente}"

@app.route("/api/consumo/rango")
def datos_ejemplo():
    electrodatos = Electrodata("electrodatos/datos/electrodatos.csv")

    id_cliente = request.args.get('cliente', type=int)
    inicio, fin = datetime.fromisoformat(request.args.get('inicio', type=str)), datetime.fromisoformat(request.args.get('fin', type=str))
    print(inicio, fin)

    series = electrodatos.cliente(id_cliente, inicio, fin)
    cadena = f"var fechas = {series[0]};\nvar datos = {series[1]};"
    return cadena
