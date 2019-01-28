from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1.0/mensaje')
def mensaje():
    return jsonify('nuevo mensaje desde el servidor Flask')


@app.route('/api/v1.0/left')
def left():
    left = request.args.get('Turn')
    return jsonify('girar a la {}').format(left)


if __name__ == '__main__':
    app.run(debug=True)
