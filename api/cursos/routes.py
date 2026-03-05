from flask import abort, redirect, render_template, request, url_for

import forms
from api.cursos import cursos
from models import Curso, Maestro, db


@cursos.route("/", methods=["GET"])
def index():
    cursos_registrados = Curso.query.order_by(Curso.id.desc()).all()
    return render_template("cursos/index.html", cursos=cursos_registrados)


@cursos.route("/agregar", methods=["GET", "POST"])
def agregar():
    maestros = Maestro.query.order_by(Maestro.nombre.asc()).all()
    if request.method == "GET":
        return render_template("cursos/agregar.html", maestros=maestros)

    create_form = forms.CursoForm(request.form)
    if not create_form.validate():
        return render_template("cursos/agregar.html", maestros=maestros, errors=create_form.errors), 400

    maestro = Maestro.query.get(create_form.maestro_id.data)
    if maestro is None:
        return render_template(
            "cursos/agregar.html",
            maestros=maestros,
            errors={"maestro_id": ["El maestro seleccionado no existe"]},
        ), 400

    nuevo_curso = Curso(
        nombre=create_form.nombre.data,
        descripcion=create_form.descripcion.data,
        maestro_id=create_form.maestro_id.data,
    )
    db.session.add(nuevo_curso)
    db.session.commit()
    return redirect(url_for("cursos.index"))


@cursos.route("/detalles", methods=["GET"])
def detalles():
    curso_id = request.args.get("id", type=int)
    curso = Curso.query.get(curso_id)
    if curso is None:
        abort(404)
    return render_template("cursos/detalles.html", curso=curso)


@cursos.route("/modificar", methods=["GET", "POST"])
def modificar():
    if request.method == "GET":
        curso_id = request.args.get("id", type=int)
        curso = Curso.query.get(curso_id)
        if curso is None:
            abort(404)
        maestros = Maestro.query.order_by(Maestro.nombre.asc()).all()
        return render_template("cursos/modificar.html", curso=curso, maestros=maestros)

    curso_id = request.form.get("id", type=int)
    curso = Curso.query.get(curso_id)
    if curso is None:
        abort(404)

    update_form = forms.CursoForm(request.form)
    maestros = Maestro.query.order_by(Maestro.nombre.asc()).all()
    if not update_form.validate():
        return render_template("cursos/modificar.html", curso=curso, maestros=maestros, errors=update_form.errors), 400

    maestro = Maestro.query.get(update_form.maestro_id.data)
    if maestro is None:
        return render_template(
            "cursos/modificar.html",
            curso=curso,
            maestros=maestros,
            errors={"maestro_id": ["El maestro seleccionado no existe"]},
        ), 400

    curso.nombre = update_form.nombre.data
    curso.descripcion = update_form.descripcion.data
    curso.maestro_id = update_form.maestro_id.data
    db.session.commit()
    return redirect(url_for("cursos.index"))


@cursos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    if request.method == "GET":
        curso_id = request.args.get("id", type=int)
        curso = Curso.query.get(curso_id)
        if curso is None:
            abort(404)
        return render_template("cursos/eliminar.html", curso=curso)

    curso_id = request.form.get("id", type=int)
    curso = Curso.query.get(curso_id)
    if curso is None:
        abort(404)

    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for("cursos.index"))
