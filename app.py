from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from api.maestros import maestros
from api.alumnos import alumnos
from api.cursos import cursos
from api.inscripciones import inscripciones
from config import DevelopmentConfig
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(alumnos, url_prefix='/alumnos')
app.register_blueprint(maestros, url_prefix='/maestros')
app.register_blueprint(cursos, url_prefix='/cursos')
app.register_blueprint(inscripciones, url_prefix='/inscripciones')

csrf = CSRFProtect(app)

csrf.init_app(app)
db.init_app(app)

with app.app_context():
	db.create_all()

migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(port=4000, debug=True)
