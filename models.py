import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Alumno(db.Model):
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apaterno = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)