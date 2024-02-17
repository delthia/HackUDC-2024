from electrodatos import app
# from electrodatos.models import Electrodata
from flask import render_template, request
from datetime import datetime
from datetime import date
from electrodatos.report_generator import ClientElectro

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
    id_cliente = request.args.get('cliente', type=int)
    electrodatos = ClientElectro(id_cliente).electro_report('Annual', 2023)
    inicio, fin = date.fromisoformat(request.args.get('inicio', type=str)), date.fromisoformat(request.args.get('fin', type=str))
    
    seleccion = ClientElectro(8).electro_report('Annual', 2023).range_consume(inicio, fin).to_dict()
    return [(seleccion['Consumo'][i], seleccion['Fecha'][i]) for i in seleccion['Consumo']]