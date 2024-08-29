from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Ayomide"))

if __name__ == "__main__":
    app.run(debug=True)