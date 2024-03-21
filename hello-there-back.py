from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)


@app.route('/api/get-value', methods=['GET'])
def get_backend_value():
    value = get_DB_val()
    return jsonify({"value": value})  # converts the dictionary to a JSON response


@app.route('/api/get-value-default', methods=['GET'])
def get_backend_value():
    value = "General Kenobi"
    return jsonify({"value": value})  # converts the dictionary to a JSON response

def get_DB_val():
    return "General Kenobi"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
