import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Alumno(db.Model):
    __tablename__ = "alumno"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Maestro(db.Model):
    __tablename__ = "maestro"

    matricula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
