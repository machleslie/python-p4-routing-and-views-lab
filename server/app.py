#!/usr/bin/env python3

from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:pr>')
def print_string (pr):
    print(pr)
    return f'{pr}'
    
@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'



    
    # for n in range(0,num):
    #     return n

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    