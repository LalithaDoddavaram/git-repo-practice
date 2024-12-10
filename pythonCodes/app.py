from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "Lakshmi" and password == "1269":
            return "Success"
        else:
            return "Failure"

@app.route("/", methods=["GET", 'POST'])
def file_upload():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return ""

if __name__ == "__main__":
    app.run(debug=True)