from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect

import forms
from config import DevelopmentConfig
from models import db, Alumno

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/alumno', methods=['GET', 'POST', 'DELETE'])
def alumno():
	if request.method == 'GET':
		return render_template('alumno.html')

	if request.method == 'POST':
		create_form = forms.UserForm(request.form)

		alumno = Alumno(nombre=create_form.nombre.data, apaterno=create_form.apaterno.data, email=create_form.email.data)
		db.session.add(alumno)
		db.session.commit()

		return redirect(url_for('index'))

	###if request.method == 'DELETE':
		alumno = Alumno(id=alumno.id)

		db.session.delete(alumno)
		db.session.commit()
		return redirect(url_for('index'))###

@app.route("/detalles", methods=['GET'])
def detalles():
	alumno = Alumno.query.get(request.args.get('id'))

	return render_template('detalles.html', nombre=alumno.nombre, apaterno=alumno.apaterno, email=alumno.email)


@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
	if (request.method == 'GET'):
		alumno = Alumno.query.get(request.args.get('id'))
		return render_template('modificar.html', alumno=alumno)

	if (request.method == 'POST'):
		create_form = forms.UserForm(request.form)

		alumno = Alumno.query.get(create_form.id.data)

		alumno.nombre = create_form.nombre.data
		alumno.apaterno = create_form.apaterno.data
		alumno.email = create_form.email.data

		db.session.commit()

		return redirect(url_for('index'))

@app.route("/")
@app.route("/index")
def index():
	create_from = forms.UserForm(request.form)
	alumno = Alumno.query.all()
	return render_template("index.html", form=create_from, alumnos=alumno)

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(port=4000, debug=True)
