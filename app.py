from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        a = data['a']
        b = data['b']
    else:
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
    result = a + b
    return jsonify(result=result)

@app.route('/subtract', methods=['GET','POST'])
def subtract():
    if request.method == 'POST':
        data = request.get_json()
        a = data['a']
        b = data['b']
    else:
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
    result = a - b
    return jsonify(result=result)

@app.route('/multiply', methods=['GET','POST'])
def multiply():
    if request.method == 'POST':
        data = request.get_json()
        a = data['a']
        b = data['b']
    else:
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
    result = a * b
    return jsonify(result=result)

@app.route('/divide', methods=['GET','POST'])
def divide():
    if request.method == 'POST':
        data = request.get_json()
        a = data['a']
        b = data['b']
    else:
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
    result = a / b
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
