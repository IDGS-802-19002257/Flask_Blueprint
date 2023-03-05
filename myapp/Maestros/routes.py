from flask import Blueprint

maestros_r = Blueprint('maestros', __name__)

@maestros_r.route('/maestros', methods = ['GET'])
def maestros():
    return { 'key':'Maestros' }