from flask import Flask,request
from flask import current_app as app

@app.route('/hello')
def hello():
    return "bbb hello"
