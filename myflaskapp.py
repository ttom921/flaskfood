from flask import Flask
import os
app= Flask(__name__)

@app.route('/')
def index():
	osconfig=os.environ['ops_config']
	return "<span style='color:red'> i am flask app 1</span>{}".format(osconfig)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)    