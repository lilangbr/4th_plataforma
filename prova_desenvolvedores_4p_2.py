from flask import Flask, jsonify
from modules_api.statistics import statistics
from modules_api.convert_types import convert_str_list


app = Flask(__name__)

@app.route("/")
def hello():
    r = {
            'How to use': 'Insert the numbers in this format: n1, n2, n3, ... in /URL_endpoint' 
    }
    return jsonify(r)

@app.route("/<vector_str>")
def major(vector_str):
    vector = convert_str_list(vector_str)
    return jsonify(statistics(vector))

@app.route("/instructions")
def how_to_use():
    r = {
            'Instructions':'You must insert numbers from 0 to 15, separated by a space, at the root of the directory: url / <insert here>. For example: 127.0.0.1:5000/3 14 2 8'
    }
    return jsonify(r)

if __name__ == '__main__':
    app.run(debug=True)
