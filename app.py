#!/usr/bin/env python3.4

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    mydata = {'lala': 77}
    return render_template("index.html", data=mydata)

@app.route("/lala", methods=['post', 'get'])
def lala():
    return render_template("index.html", data={'lala': request.form['opa']})

@app.route("/lolo")
def lolo():
    return "OOOOOpa!"

if __name__ == "__main__":
    app.run(debug=True) 
