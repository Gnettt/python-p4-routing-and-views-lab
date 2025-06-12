#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return f'<h1>Printed: {string}</h1>'

@app.route('/count/<int:number>')
def count(number):
    numbers = '<br>'.join(str(i) for i in range(number))
    return f'<h1>Counting to {number}</h1><p>{numbers}</p>'


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = 'undefined' if num2 == 0 else num1 / num2
    elif operation == '%':
        result = 'undefined' if num2 == 0 else num1 % num2
    else:
        return '<h1>Invalid operation</h1>'

    return f'''
        <h1>Math Operation</h1>
        <p>{num1} {operation} {num2} = {result}</p>
    '''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
