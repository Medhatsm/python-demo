from flask import Flask, request, jsonify, render_template
import importlib
app = Flask(__name__)

@app.route('/')
def index():
    for i in range(1, 61):
        module_name = f"file{i}"
        module = importlib.import_module(module_name)
        method1 = getattr(module, "method1")
        method1()

    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero is not allowed"
    else:
        result = "Invalid operation"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
