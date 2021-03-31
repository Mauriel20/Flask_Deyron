"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
import json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Paciente, Hospital, Doctor
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# Todo lo relacionado con paciente
@app.route('/paciente', methods=['GET'])
def get_users():
    user = Paciente.query.all()
    mapeo= list(map(lambda x: x.serialize(),user))
    return jsonify(mapeo), 200


@app.route('/paciente/<int:id_get>', methods=['GET'])
def get_with_id(id_get):
    usuario = Paciente.query.get(id_get)
    usuario_final= usuario.serialize()
    return jsonify(usuario_final), 200

@app.route('/paciente', methods=['POST'])
def add_user():
   
    request_body = json.loads(request.data)

    if request_body["name"] == None and request_body["last_name"] == None and request_body["suffering"] == None:
        return "Datos incompletos"
    else:

        user = Paciente(name=request_body["name"], last_name=request_body["last_name"], suffering=request_body["suffering"])
        db.session.add(user)
        db.session.commit()
        return "Posteo exitoso"
    
@app.route('/paciente/<int:DNI>', methods=['DELETE'])
def delete_user_by_id(DNI):
    user = Paciente.query.filter_by(DNI=DNI).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return("User has been deleted successfully"), 200

# Todo relacionado con doctor
@app.route('/doctor', methods=['GET'])
def get_users_doctors():
    user = Doctor.query.all()
    mapeo= list(map(lambda x: x.serialize(),user))
    return jsonify(mapeo), 200


@app.route('/doctor/<int:id_get>', methods=['GET'])
def get_with_id_doctor(id_get):
    usuario = Doctor.query.get(id_get)
    usuario_final= usuario.serialize()
    return jsonify(usuario_final), 200

@app.route('/doctor', methods=['POST'])
def add_user_doctors():
   
    request_body = json.loads(request.data)

    if request_body["name"] == None and request_body["last_name"] == None and request_body["Especialidad"] == None:
        return "Datos incompletos"
    else:

        user = Doctor(name=request_body["name"], last_name=request_body["last_name"], Especialidad=request_body["Especialidad"])
        db.session.add(user)
        db.session.commit()
        return "Posteo exitoso"
    
@app.route('/doctor/<int:DNI_doctor>', methods=['DELETE'])
def delete_user_by_id_doctors(DNI_doctor):
    user = Doctor.query.filter_by(DNI_doctor=DNI_doctor).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return("User has been deleted successfully"), 200

# Todo relacionado con hospital

@app.route('/hospital', methods=['GET'])
def get_users_hospital():
    user = Hospital.query.all()
    mapeo= list(map(lambda x: x.serialize(),user))
    return jsonify(mapeo), 200


@app.route('/hospital/<int:id_get>', methods=['GET'])
def get_with_id_hospital(id_get):
    usuario = Hospital.query.get(id_get)
    usuario_final= usuario.serialize()
    return jsonify(usuario_final), 200

@app.route('/hospital', methods=['POST'])
def add_user_hospital():
   
    request_body = json.loads(request.data)

    # if request_body["birth"] :
    #     return "Datos incompletos"
    # else:

    user = Hospital(birth=request_body["birth"], DNI_paciente_hospital=request_body["DNI_paciente_hospital"], DNI_doctor_hospital=request_body["DNI_doctor_hospital"])
    db.session.add(user)
    db.session.commit()
    return "Posteo exitoso"
    
@app.route('/hospital/<int:DNI_cita>', methods=['DELETE'])
def delete_user_by_id_hospital(DNI_cita):
    user = Hospital.query.filter_by(DNI_cita=DNI_cita).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return("User has been deleted successfully"), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
