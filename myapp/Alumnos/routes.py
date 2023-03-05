from flask import Blueprint

alumnos_r = Blueprint('alumnos', __name__)

@alumnos_r.route('/alumnos', methods = ['GET'])
def alumnos():
    return { 'key':'Alumnos' }