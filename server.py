import os

from flask import Flask, render_template, request
from maths.mathematics import MathOperations

os.chdir("E:\COURSERA\PythonFlask\week_2\hjbsk-build_deploy_app_flask")

app = Flask("Mathematics Problem Solver")


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/sum")
def sum_route():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))

    math_solver = MathOperations()
    result = math_solver.summation(num1, num2)
    return f"The sum of {num1} and {num2} is {result}"


@app.route("/sub")
def sub_route():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))

    math_solver = MathOperations()
    result = math_solver.subtraction(num1, num2)
    return f"The difference of {num1} and {num2} is {result}"


@app.route("/mul")
def mul_route():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))

    math_solver = MathOperations()
    result = math_solver.multiplication(num1, num2)
    return f"The product of {num1} and {num2} is {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
