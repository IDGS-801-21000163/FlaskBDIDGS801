from wtforms import Form, IntegerField, validators, StringField


class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=0, max=20, message='Please enter a valid id.')])
    nombre = StringField('nombre', [
        validators.DataRequired('Please enter a valid nombre.'),
        validators.Length(min=4, max=20, message='Please enter a valid nombre.')
    ])

    apaterno = StringField('apaterno', [
        validators.DataRequired('Please enter a valid apaterno.'),
    ])

    email = StringField('email', [
        validators.DataRequired('Please enter a valid email.'),
        validators.Email('Please enter a valid email.')
    ])