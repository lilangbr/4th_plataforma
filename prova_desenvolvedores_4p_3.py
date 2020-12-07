from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    r = {
            'Msg':'Welcome to the 3rd challenge!'
    }
    return jsonify(r)

@app.route("/scores")
def scores():
    r = {
            'scores':'complete'
    }
    return jsonify(r)

@app.route("/bestslaps")
def bestslaps():
    r = {
            'bestslaps':'complete'
    }
    return jsonify(r)

@app.route("/bestlap")
def bestlap():
    r = {
            'bestlap':'complete'
    }
    return jsonify(r)

@app.route("/average_speeds")
def average_speeds():
    r = {
            'average_speeds':'complete'
    }
    return jsonify(r)

if __name__ == '__main__':
    app.run(debug=True)

