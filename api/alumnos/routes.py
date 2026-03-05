from flask import abort, redirect, render_template, request, url_for

import forms
from models import Alumno, db
from api.alumnos import alumnos


@alumnos.route("/", methods=["GET"])
def alumno():
    alumnos_registrados = Alumno.query.all()
    return render_template("alumnos/index.html", alumnos=alumnos_registrados)


@alumnos.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template("alumnos/agregar.html")

    create_form = forms.AlumnoForm(request.form)
    if not create_form.validate():
        print(create_form.errors)
        return render_template("alumnos/agregar.html", errors=create_form.errors), 400

    nuevo_alumno = Alumno(
        nombre=create_form.nombre.data,
        apellidos=create_form.apellidos.data,
        email=create_form.email.data,
        telefono=create_form.telefono.data,
    )
    db.session.add(nuevo_alumno)
    db.session.commit()

    return redirect(url_for("alumnos.alumno"))


@alumnos.route("/detalles", methods=["GET"])
def detalles():
    alumno_id = request.args.get("id", type=int)
    alumno = Alumno.query.get(alumno_id)
    if alumno is None:
        abort(404)
    return render_template("alumnos/detalles.html", alumno=alumno)


@alumnos.route("/modificar", methods=["GET", "POST"])
def modificar():
    if request.method == "GET":
        alumno_id = request.args.get("id", type=int)
        alumno = Alumno.query.get(alumno_id)
        if alumno is None:
            abort(404)
        return render_template("alumnos/modificar.html", alumno=alumno)

    update_form = forms.AlumnoForm(request.form)
    if not update_form.validate():
        alumno = Alumno.query.get(request.form.get("id", type=int))
        return render_template("alumnos/modificar.html", alumno=alumno, errors=update_form.errors), 400

    alumno = Alumno.query.get(request.form.get("id", type=int))
    if alumno is None:
        abort(404)

    alumno.nombre = update_form.nombre.data
    alumno.apellidos = update_form.apellidos.data
    alumno.email = update_form.email.data
    alumno.telefono = update_form.telefono.data
    db.session.commit()

    return redirect(url_for("alumnos.alumno"))


@alumnos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    if request.method == "GET":
        alumno_id = request.args.get("id", type=int)
        alumno = Alumno.query.get(alumno_id)
        if alumno is None:
            abort(404)
        return render_template("alumnos/eliminar.html", alumno=alumno)

    alumno_id = request.form.get("id", type=int)
    alumno = Alumno.query.get(alumno_id)
    if alumno is None:
        abort(404)

    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for("alumnos.alumno"))
