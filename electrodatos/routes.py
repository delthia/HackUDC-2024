from electrodatos import app
from flask import render_template, request, Response
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
    return render_template("cliente.html", cliente = id_cliente, year = 2023, meses=api_anos(id_cliente, 2023), mes=api_rango(id_cliente, date(2023,2,1), date(2023, 2, 28)), horario=api_dia(id_cliente, 2023), semanal=api_semana(id_cliente, 2023))

def api_rango(id_cliente, inicio, fin):
    seleccion = ClientElectro(id_cliente).electro_report().range_consume(inicio, fin).to_dict()
    return {'fechas': [ seleccion['Fecha'][i].strftime("%B %d, %Y") for i in seleccion['Fecha'] ], 'datos': [ seleccion['Consumo'][i] for i in seleccion['Consumo'] ]}

def api_anos(id_cliente, year):    
    years = ClientElectro(id_cliente).electro_report('Annual', year=year).annual_comparison.to_dict()

    return {'curr': list(years[f'Consumo_{year}'].values()), 'prev': list(years[f'Consumo_{year-1}'].values())}


def api_semana(id_cliente, ano):
    consumo = ClientElectro(id_cliente).electro_report('Annual', year=ano).weekday_comparison.to_dict()['Consumo']

    return [ consumo[i] for i in consumo]

def api_dia(id_cliente, ano):
    # dia = list(ClientElectro(id_cliente).electro_report('Annual', year = ano).max_consumption.to_dict()['Consumo'].values())
    dia = ClientElectro(id_cliente).electro_report('Annual', year=ano).max_consumption

    return [sum(dia[i:i+6]) for i in range(0, 24, 6)]


@app.route("/api/htmx/grafico_anual/<int:year>/<int:id_cliente>")
def grafico_anual(year, id_cliente):
    return render_template('graph_anual.html', year=year, cliente=id_cliente, datos=api_anos(id_cliente, year))
