from flask import abort, redirect, render_template, request, url_for

import forms
from api.maestros import maestros
from models import Maestro, db


@maestros.route("/", methods=["GET"])
def maestro():
    maestros_registrados = Maestro.query.all()
    return render_template("maestros/index.html", maestros=maestros_registrados)


@maestros.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template("maestros/agregar.html")

    create_form = forms.MaestroForm(request.form)
    if not create_form.validate():
        return render_template("maestros/agregar.html", errors=create_form.errors), 400

    maestro_existente = Maestro.query.filter_by(
        matricula=create_form.matricula.data
    ).first()

    if maestro_existente:
        return render_template(
            "maestros/agregar.html",
            errors={"matricula": ["La matrícula ya está registrada"]}
        )

    nuevo_maestro = Maestro(
        matricula=create_form.matricula.data,
        nombre=create_form.nombre.data,
        apellidos=create_form.apellidos.data,
        especialidad=create_form.especialidad.data,
        email=create_form.email.data,
    )
    db.session.add(nuevo_maestro)
    db.session.commit()
    return redirect(url_for("maestros.maestro"))


@maestros.route("/detalles", methods=["GET"])
def detalles():
    matricula = request.args.get("matricula", type=int)
    maestro = Maestro.query.get(matricula)
    if maestro is None:
        abort(404)
    return render_template("maestros/detalles.html", maestro=maestro)


@maestros.route("/modificar", methods=["GET", "POST"])
def modificar():
    if request.method == "GET":
        matricula = request.args.get("matricula", type=int)
        maestro = Maestro.query.get(matricula)
        if maestro is None:
            abort(404)
        return render_template("maestros/modificar.html", maestro=maestro)

    update_form = forms.MaestroForm(request.form)
    if not update_form.validate():
        maestro = Maestro.query.get(request.form.get("matricula", type=int))
        return render_template("maestros/modificar.html", maestro=maestro, errors=update_form.errors), 400

    maestro = Maestro.query.get(update_form.matricula.data)
    if maestro is None:
        abort(404)

    maestro.nombre = update_form.nombre.data
    maestro.apellidos = update_form.apellidos.data
    maestro.especialidad = update_form.especialidad.data
    maestro.email = update_form.email.data
    db.session.commit()

    return redirect(url_for("maestros.maestro"))


@maestros.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    if request.method == "GET":
        matricula = request.args.get("matricula", type=int)
        maestro = Maestro.query.get(matricula)
        if maestro is None:
            abort(404)
        return render_template("maestros/eliminar.html", maestro=maestro)

    matricula = request.form.get("matricula", type=int)
    maestro = Maestro.query.get(matricula)
    if maestro is None:
        abort(404)

    db.session.delete(maestro)
    db.session.commit()
    return redirect(url_for("maestros.maestro"))
