from flask import Blueprint, request, jsonify
from services.cloudinary_service import transform

main = Blueprint('index_blueprint', __name__)

@main.route('/hi', methods=['GET'])
def say_hello():
    return "Hello World"

@main.route('/upload', methods=['Post'])
def index():
    if 'file' not in request.files:
        print("error file")
        return jsonify({"error": "No se encontró un archivo en la solicitud"}), 400
    if 'costume' not in request.form:
        print("error costume")
        return jsonify({"error": "Faltan campos en el formulario"}), 400
    file = request.files['file']
    costume=request.form['costume']
    response=transform(file=file,costume=costume)
    return jsonify({"response":response})


