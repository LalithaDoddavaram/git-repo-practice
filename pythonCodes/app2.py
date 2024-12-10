from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/request")
def status():
    response = make_response('Hello World')
    response.statuscode = 202
    response.headers['content-type'] = "text/plain"
    return response

@app.route("/hello", methods = ["POST", 'GET', 'PUT'])
def req():
    if request.method == 'GET':
        return "You made a GET request"
    elif request.method == 'POST':
        return "You made a POST request"
    else:
        return "You will never see this message"

@app.route('/handle_params')
def handles_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        name = request.args.get('name')
        greeting = request.args['greeting']

        return f"Good {greeting}, {name}"
    else:
        return "Some parameters are missing"

@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route("/greet/<name>")
def greet_name(name):
    return f"Hello {name}"

@app.route("/", methods = ['POST', 'GET'])
def greet():
    return "Hello!!!"

if __name__ == "__main__":
    app.run(debug=True)