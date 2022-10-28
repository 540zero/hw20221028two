from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>00求職中界點</h1>"
	homepage += "<a href=/main>首頁</a><br>"
	homepage += "<a href=/Application>想要的結果</a><br>"
	homepage += "<a href=/CareerResults>職涯結果</a><br>"
	homepage += "<a href=/Resume>求職履歷自傳</a><br>"
	return homepage

@app.route("/main")
def welcome():
	return render_template("main.html")

@app.route("/Application")
def Application():
	return render_template("Application.html")

@app.route("/CareerResults")
def CareerResults():
	return render_template("CareerResults.html")

@app.route("/Resume")
def Resume():
	return render_template("Resume.html")

#if __name__ == "__main__":
#	app.run()