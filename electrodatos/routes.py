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
def api_rango():
    id_cliente = request.args.get('cliente', type=int)
    electrodatos = ClientElectro(id_cliente).electro_report('Annual', 2023)
    inicio, fin = date.fromisoformat(request.args.get('inicio', type=str)), date.fromisoformat(request.args.get('fin', type=str))
    
    seleccion = ClientElectro(id_cliente).electro_report('Annual', 2023).range_consume(inicio, fin).to_dict()
    return f"fechas = {[ str(seleccion['Fecha'][i]) for i in seleccion['Fecha'] ]}; datos = {[ seleccion['Consumo'][i] for i in seleccion['Consumo'] ]};"

@app.route("/api/consumo/dia")
def api_dia():
    id_cliente = request.args.get('cliente', type=int)
    fecha = date.fromisoformat(request.args.get('fecha', type=str))
    dia = ClientElectro(id_cliente).electro_report('Day', date=fecha).day_db

    print(dia)

    return f"consumos = {[sum(dia[i:i+6]) for i in range(0, 24, 6)]};"

@app.route("/api/consumo/ano")
def api_ano():
    id_cliente = request.args.get('cliente', type=int)
    year = request.args.get('ano', type=int)
    ano = ClientElectro(id_cliente).electro_report('Annual', year=year).monthly_comparison

    d = ano.to_dict()['Consumo']
    # return [ d[i] if i in d.keys() else 0 for i in range(1, 13)]
    return [d[i] for i in d]

@app.route("/api/consumo/comp_anos")
def api_anos():
    id_cliente = request.args.get('cliente', type=int)
    year = request.args.get('ano', type=int)
    
    years = ClientElectro(id_cliente).electro_report('Annual', year=year).annual_comparison.to_dict()

    return f"curr = {list(years[f'Consumo_{year}'].values())}; prev = {list(years[f'Consumo_{year-1}'].values())};"

@app.route("/api/consumo/dia_semana")
def api_semana():
    id_cliente = request.args.get('cliente', type=int)
    mes = request.args.get('ano', type=int)
    ano = request.args.get('mes', type=int)

    consumo = ClientElectro(id_cliente).electro_report('Monthly', year=ano, month=mes).week_comparison.to_dict()['Consumo']
    print(consumo)
    # return f"semanal = {[ consumo[i] if i in consumo.keys() else 0 for i in range(0, 7)]};"
    return f"semanal = {[ consumo[i] for i in consumo]}"
    # return ClientElectro(id_cliente).electro_report('Monthly', year=ano, month=mes).week_comparison.to_dict()
