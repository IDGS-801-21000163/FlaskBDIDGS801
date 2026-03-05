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

    inscripciones = db.relationship(
        "Inscripcion",
        back_populates="alumno",
        cascade="all, delete-orphan",
    )


class Maestro(db.Model):
    __tablename__ = "maestro"

    matricula = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    cursos = db.relationship(
        "Curso",
        back_populates="maestro",
        cascade="all, delete-orphan",
    )


class Curso(db.Model):
    __tablename__ = "curso"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    maestro_id = db.Column(db.Integer, db.ForeignKey("maestro.matricula"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    maestro = db.relationship("Maestro", back_populates="cursos")
    inscripciones = db.relationship(
        "Inscripcion",
        back_populates="curso",
        cascade="all, delete-orphan",
    )


class Inscripcion(db.Model):
    __tablename__ = "inscripcion"
    __table_args__ = (
        db.UniqueConstraint("alumno_id", "curso_id", name="uq_inscripcion_alumno_curso"),
    )

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey("alumno.id"), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    alumno = db.relationship("Alumno", back_populates="inscripciones")
    curso = db.relationship("Curso", back_populates="inscripciones")
