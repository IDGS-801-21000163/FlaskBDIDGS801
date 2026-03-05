from wtforms import EmailField, Form, IntegerField, StringField, validators


class AlumnoForm(Form):
    nombre = StringField(
        "nombre",
        [
            validators.DataRequired(message="El nombre es requerido"),
            validators.Length(min=2, max=100, message="El nombre debe tener entre 2 y 100 caracteres"),
        ],
    )
    apellidos = StringField(
        "apellidos",
        [
            validators.DataRequired(message="Los apellidos son requeridos"),
            validators.Length(min=2, max=200, message="Los apellidos deben tener entre 2 y 200 caracteres"),
        ],
    )
    email = EmailField(
        "email",
        [
            validators.DataRequired(message="El correo es requerido"),
            validators.Email(message="Ingrese un correo valido"),
            validators.Length(max=150, message="El correo no debe exceder 150 caracteres"),
        ],
    )
    telefono = StringField(
        "telefono",
        [
            validators.DataRequired(message="El telefono es requerido"),
            validators.Length(min=10, max=20, message="El telefono debe tener entre 10 y 20 caracteres"),
        ],
    )


class MaestroForm(Form):
    matricula = IntegerField(
        "matricula",
        [
            validators.DataRequired(message="La matricula es requerida"),
            validators.NumberRange(min=1, message="La matricula debe ser mayor a 0"),
        ],
    )
    nombre = StringField(
        "nombre",
        [
            validators.DataRequired(message="El nombre es requerido"),
            validators.Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres"),
        ],
    )
    apellidos = StringField(
        "apellidos",
        [
            validators.DataRequired(message="Los apellidos son requeridos"),
            validators.Length(min=2, max=50, message="Los apellidos deben tener entre 2 y 50 caracteres"),
        ],
    )
    especialidad = StringField(
        "especialidad",
        [
            validators.DataRequired(message="La especialidad es requerida"),
            validators.Length(min=2, max=50, message="La especialidad debe tener entre 2 y 50 caracteres"),
        ],
    )
    email = EmailField(
        "email",
        [
            validators.DataRequired(message="El correo es requerido"),
            validators.Email(message="Ingrese un correo valido"),
            validators.Length(max=50, message="El correo no debe exceder 50 caracteres"),
        ],
    )


class CursoForm(Form):
    nombre = StringField(
        "nombre",
        [
            validators.DataRequired(message="El nombre del curso es requerido"),
            validators.Length(min=2, max=150, message="El nombre del curso debe tener entre 2 y 150 caracteres"),
        ],
    )
    descripcion = StringField(
        "descripcion",
        [
            validators.DataRequired(message="La descripcion es requerida"),
            validators.Length(min=5, message="La descripcion debe tener al menos 5 caracteres"),
        ],
    )
    maestro_id = IntegerField(
        "maestro_id",
        [
            validators.DataRequired(message="El maestro es requerido"),
            validators.NumberRange(min=1, message="Maestro invalido"),
        ],
    )


class InscripcionForm(Form):
    alumno_id = IntegerField(
        "alumno_id",
        [
            validators.DataRequired(message="El alumno es requerido"),
            validators.NumberRange(min=1, message="Alumno invalido"),
        ],
    )
    curso_id = IntegerField(
        "curso_id",
        [
            validators.DataRequired(message="El curso es requerido"),
            validators.NumberRange(min=1, message="Curso invalido"),
        ],
    )
