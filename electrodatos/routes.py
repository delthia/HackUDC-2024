from electrodatos import app

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
