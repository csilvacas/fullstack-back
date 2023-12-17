""" Creacion de Pedidos """
from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza")

@app.route("/pizza", methods=['POST'])
def recibir_pedido():
    """ Procesar Formulario """
    # Procesar los datos del formulario enviado por POST
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")

    # Guardar los datos en un archivo: pedidos.txt
    guardar_pedido(nombre, apellidos)

    # Imprimir los valores para que se vea en la consola Python.
    print(nombre + " " + apellidos)
    print("Pedido guardado correctamente en pedidos.txt")

    # Devuelve una respuesta, con una redirección a “solicita_pedido.html”
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize", methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get('tamano')      
    if size == 'S':
        mensaje = 'No disponible'
    else:
        mensaje = 'Disponible'

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
