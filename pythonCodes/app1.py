from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.template_filter("repeat")
def repeat(s, times=2):
    return s * times

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.route("/")
def new_page():
    arg1 = [10, 20, 30, 40, 50]
    return render_template("index.html", arg1=arg1)

@app.route("/filters")
def filter():
    some_text = "Hello World"
    return render_template("filter.html", some_text=some_text)

if __name__ == "__main__":
    app.run(debug=True)