from flask import Flask, request, jsonify, render_template
import importlib
app = Flask(__name__)

@app.route('/')
def index():
    for i in range(1, 101):
        module_name = f"file{i}"
        module = importlib.import_module(module_name)
        method1 = getattr(module, "method1")
        method1()

    return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     operation = data['operation']

#     if operation == 'add':
#         result = num1 + num2
#     elif operation == 'subtract':
#         result = num1 - num2
#     elif operation == 'multiply':
#         result = num1 * num2
#     elif operation == 'divide':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             result = "Division by zero is not allowed"
#     else:
#         result = "Invalid operation"

#     return jsonify({'result': result})

# @app.route('/')
# def index():
#     return 'Welcome to Simple Calculator!'

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    numbers = data.get('numbers', [])
    result = sum(numbers)
    for i in range(300):
        for i in range(1, 301):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()    
        for i in range(1, 200):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()
        for i in range(1, 301):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()    
        for i in range(1, 301):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()                   
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    numbers = data.get('numbers', [])
    result = numbers[0] - sum(numbers[1:])
    for i in range(300):
        for i in range(100, 200):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()    
        for i in range(1, 200):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()
        for i in range(150, 201):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()    
        for i in range(200, 250):
            module_name = f"file{i}"
            module = importlib.import_module(module_name)
            method1 = getattr(module, "method1")
            method1()       
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    numbers = data.get('numbers', [])
    result = 1
    for num in numbers:
        result *= num
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    numbers = data.get('numbers', [])
    if 0 in numbers[1:]:
        return jsonify({'error': 'Cannot divide by zero!'})
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return jsonify({'result': result})   


if __name__ == '__main__':
    app.run(debug=True)
