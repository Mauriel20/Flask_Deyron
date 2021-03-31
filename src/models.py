from flask_sqlalchemy import SQLAlchemy
import os
from flask_admin import Admin
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DATETIME
from flask_admin.contrib.sqla import ModelView
from datetime import datetime, timezone, timedelta
db = SQLAlchemy()

class Paciente(db.Model):
    DNI = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    suffering = db.Column(db.String(80), unique=False, nullable=False)
   
    # favorites= db.relationship('Favorites', lazy=True)
    # def __repr__(self):
    #     return '<User %r>' % self.name 

    def serialize(self):
        return {
            "DNI": self.DNI,
            "name": self.name,
            "last_name": self.last_name,
            "suffering": self.suffering,
          
          
            
            # do not serialize the password, its a security breach
        }
class Doctor(db.Model):
    DNI_doctor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    Especialidad = db.Column(db.String(120), unique=False, nullable=False)
    
   
    # DNI_doctor_hospital = db.Column(db.Integer, db.ForeignKey(Paciente.DNI))

    def serialize(self):
        return {
            "DNI_doctor": self.DNI_doctor,
            "name": self.name,
            "last_name": self.last_name,
            "Especialidad": self.Especialidad,
            # "type": self.type,
            # do not serialize the password, its a security breach
        }
       
     
        
class Hospital(db.Model):
    DNI_cita = db.Column(db.Integer, primary_key=True)
    birth = db.Column(DATETIME)
    DNI_paciente_hospital = db.Column(db.Integer, db.ForeignKey(Paciente.DNI))
    DNI_doctor_hospital = db.Column(db.Integer, db.ForeignKey(Doctor.DNI_doctor))
    # DNI_doctor_hospital = db.Column(db.Integer, db.ForeignKey(Paciente.DNI))

    def serialize(self):
        return {
            "DNI_cita": self.DNI_cita,
            "birth": self.birth,
            "DNI_paciente_hospital": self.DNI_paciente_hospital,
            "DNI_doctor_hospital": self. DNI_doctor_hospital,
            # "type": self.type,
            # do not serialize the password, its a security breach
        }
