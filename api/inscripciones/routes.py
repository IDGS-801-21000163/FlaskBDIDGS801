from flask import abort, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

import forms
from api.inscripciones import inscripciones
from models import Alumno, Curso, Inscripcion, db


@inscripciones.route("/", methods=["GET"])
def index():
    inscripciones_registradas = Inscripcion.query.order_by(Inscripcion.id.desc()).all()
    return render_template("inscripciones/index.html", inscripciones=inscripciones_registradas)


@inscripciones.route("/agregar", methods=["GET", "POST"])
def agregar():
    alumnos = Alumno.query.order_by(Alumno.nombre.asc()).all()
    cursos = Curso.query.order_by(Curso.nombre.asc()).all()

    if request.method == "GET":
        return render_template("inscripciones/agregar.html", alumnos=alumnos, cursos=cursos)

    create_form = forms.InscripcionForm(request.form)
    if not create_form.validate():
        return render_template(
            "inscripciones/agregar.html",
            alumnos=alumnos,
            cursos=cursos,
            errors=create_form.errors,
        ), 400

    alumno = Alumno.query.get(create_form.alumno_id.data)
    curso = Curso.query.get(create_form.curso_id.data)
    if alumno is None or curso is None:
        return render_template(
            "inscripciones/agregar.html",
            alumnos=alumnos,
            cursos=cursos,
            errors={"inscripcion": ["Alumno o curso invalido"]},
        ), 400

    nueva_inscripcion = Inscripcion(
        alumno_id=create_form.alumno_id.data,
        curso_id=create_form.curso_id.data,
    )
    db.session.add(nueva_inscripcion)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return render_template(
            "inscripciones/agregar.html",
            alumnos=alumnos,
            cursos=cursos,
            errors={"inscripcion": ["El alumno ya esta inscrito en este curso"]},
        ), 400

    return redirect(url_for("inscripciones.index"))


@inscripciones.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    if request.method == "GET":
        inscripcion_id = request.args.get("id", type=int)
        inscripcion = Inscripcion.query.get(inscripcion_id)
        if inscripcion is None:
            abort(404)
        return render_template("inscripciones/eliminar.html", inscripcion=inscripcion)

    inscripcion_id = request.form.get("id", type=int)
    inscripcion = Inscripcion.query.get(inscripcion_id)
    if inscripcion is None:
        abort(404)

    db.session.delete(inscripcion)
    db.session.commit()
    return redirect(url_for("inscripciones.index"))
