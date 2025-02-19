from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template("index.html")

@app.route("/aboutme")
def aboutme():
	return render_template("aboutme.html")

@app.route("/baja")
def baja():
	return render_template("baja.html")

@app.route("/resume")
def resume():
	return render_template("resume.html")
