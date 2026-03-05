from flask import Blueprint

alumnos=Blueprint(
    'alumnos',
    __name__,
    template_folder='templates/alumnos',
    static_folder='static')
from . import routes