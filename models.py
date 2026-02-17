import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Alumno(db.Model):
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apaterno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)