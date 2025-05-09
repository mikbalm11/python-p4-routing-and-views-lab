#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ""
    for i in range(parameter):
        output += f"{i}\n"
    return f'{output}'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # num1, operation, num2
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        print("incorrect math operation")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
