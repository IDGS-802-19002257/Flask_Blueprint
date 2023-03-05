from flask import Blueprint

directivos_r = Blueprint('directivos', __name__)

@directivos_r.route('/directivos', methods = ['GET'])
def directivos():
    return { 'key':'Directivos' }