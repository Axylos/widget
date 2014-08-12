#!flask/bin/python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('widget.html')


@app.route('/_tasks')
def tasks():
  data = {"task_status": { "Search": "complete",
            "Profile": "incomplete",
            "Opportunities": "incomplete"} }
  return jsonify(data)

@app.route('/_othertasks')
def othertasks():
	data ={"task_status": {"Search": "incomplete",
				"Transaction Profile": "complete",
				"Profile": "incomplete" } }
	return jsonify(data)


