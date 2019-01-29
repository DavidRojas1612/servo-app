from flask import Flask, jsonify, request, render_template
from werkzeug.datastructures import MultiDict, CombinedMultiDict
from flask_cors import CORS

app = Flask(__name__,
            static_folder='./front/static',
            template_folder='./front')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1.0/mensaje')
def mensaje():
    return jsonify('nuevo mensaje desde el servidor Flask')


@app.route('/api/v1.0/left', methods=['POST', 'GET'])
def left():
    if request.method == 'GET':
        degrees = request.args.get('turn')
        return jsonify('girando a la izquierda')


@app.route('/api/v1.0/right', methods=['POST', 'GET'])
def right():
    if request.method == 'GET':
        degrees = request.args.get('turn')
        return jsonify('girando a la derecha')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_react(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
