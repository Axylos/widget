from flask import Flask, render_template, request, jsonify

app - Flask(__name__)

@app.route('/')
def index():
  return render_template('widget.html')


@app.route('/_tasks')
def tasks():
  return jsonify(arr=["arr", 2])

if __name__ = '__main__':
  app.run(
    host="0.0.0.0",
    port=int("80"),
    debug=True
  )

