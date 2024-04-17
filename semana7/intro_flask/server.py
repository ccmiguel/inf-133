
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"


@app.route("/saludar", methods=["GET"])
def saludar():
    
    nombre = request.args.get("nombre")
    
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})


@app.route("/sumar", methods=["POST"])  # Cambio a POST
def sumar():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    
    if num1 is None or num2 is None:
        return jsonify({"error": "Se requieren dos números en el cuerpo de la solicitud."}), 400
    
    try:
        resultado = int(num1) + int(num2)
        return jsonify({"resultado": resultado}), 200
    except ValueError:
        return jsonify({"error": "Los valores proporcionados no son números válidos."}), 400


@app.route("/palindromo", methods=["POST"])  # Cambio a POST
def palindromo():
    data = request.json
    cadena = data.get("cadena")
    
    if not cadena:
        return jsonify({"error": "Se requiere una cadena en el cuerpo de la solicitud."}), 400
    
    if cadena == cadena[::-1]:
        return jsonify({"mensaje": f"La cadena '{cadena}' es un palíndromo."}), 200
    else:
        return jsonify({"mensaje": f"La cadena '{cadena}' no es un palíndromo."}), 200


@app.route("/contar", methods=["POST"])  # Cambio a POST
def contar():
    data = request.json
    cadena = data.get("cadena")
    vocal = data.get("vocal")
    
    if not cadena or not vocal:
        return jsonify({"error": "Se requiere una cadena y una vocal en el cuerpo de la solicitud."}), 400
    
    count = cadena.count(vocal)
    return jsonify({"resultado": count}), 200

if __name__ == "__main__":
    app.run()





