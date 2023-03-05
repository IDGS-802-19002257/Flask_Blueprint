import flask

from Alumnos.routes import alumnos_r
from Directivos.routes import directivos_r
from Maestros.routes import maestros_r

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
    return flask.jsonify({'principal':'HOME'})

app.register_blueprint(alumnos_r)
app.register_blueprint(directivos_r)
app.register_blueprint(maestros_r)

if __name__ == '__main__':
    app.run()