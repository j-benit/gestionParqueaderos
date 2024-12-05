import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Página principal (puede redirigir a registro)
@app.route("/")
def index():
    return render_template("index.html")

# Página para la vista de pagos, con los botones que redirigen a las otras páginas
@app.route("/pagos")
def pagos():
    return render_template("pagos.html")

# Página para registrar pagos
@app.route("/registrar", methods=['GET', 'POST'])
def registrar_pago():
    if request.method == 'POST':
        numero_tarjeta = request.form.get('cardNumber')
        nombre_tarjeta = request.form.get('cardName')
        fecha = request.form.get('date')

        # Validación básica
        if not numero_tarjeta or not nombre_tarjeta or not fecha:
            return "Error: Datos incompletos.", 400

        # Guardar el pago en un archivo
        with open("pagos.txt", "a") as archivo:
            archivo.write(f"Número de Tarjeta: {numero_tarjeta}, Nombre: {nombre_tarjeta}, Fecha: {fecha}\n")

        return "Pago registrado exitosamente."
    return render_template("registrar.html")

# Página para actualizar pagos
@app.route("/actualizarPagos", methods=['GET', 'POST'])
def actualizar_pago():
    if request.method == 'POST':
        # Implementar lógica para actualizar un pago
        return "Pago actualizado exitosamente."
    return render_template("actualizarPagos.html")

# Página para ver historial de pagos
@app.route("/historial", methods=['GET'])
def historial_pagos():
    datos = []
    if os.path.exists("pagos.txt"):
        with open("pagos.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(", ")
                pago = {parte.split(": ")[0]: parte.split(": ")[1] for parte in partes}
                datos.append(pago)
    return render_template("historial.html", pagos=datos)

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
