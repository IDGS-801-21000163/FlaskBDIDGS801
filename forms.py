from wtforms import Form, IntegerField, validators, StringField


class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=0, max=20, message='Please enter a valid id.')])
    nombre = StringField('nombre', [
        validators.DataRequired('Please enter a valid nombre.'),
        validators.Length(min=4, max=20, message='Please enter a valid nombre.')
    ])

    apellidos = StringField('apellidos', [
        validators.DataRequired('Please enter a valid apellidos.'),
    ])

    email = StringField('email', [
        validators.DataRequired('Please enter a valid email.'),
        validators.Email('Please enter a valid email.')
    ])

    telefono = StringField('telefono', [
        validators.DataRequired('Please enter a valid telefono.'),
        validators.Length(min=10, max=10, message='Please enter a valid telefono.')
    ])