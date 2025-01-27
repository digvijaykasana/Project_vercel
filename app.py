from flask import Flask, request, jsonify, render_template
from calculator import handle_calculate
from string_utils import handle_string_util

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_request():
    action = request.form['action']
    data = request.form['data']

    if action == 'calculate':
        result = handle_calculate(data)
        return jsonify({"result": result}), 200
    elif action == 'string_util':
        result = handle_string_util(data)
        return jsonify({"result": result}), 200
    else:
        return jsonify({"error": "Invalid action specified"}), 400


if __name__ == '__main__':
    app.run()  


#if __name__ == '__main__':
 #   app.run(debug=True, port=5001)  # You can change the port as needed
