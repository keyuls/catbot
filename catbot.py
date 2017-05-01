from flask import Flask,request
import apiConnect as ac
import facebookResponse as fr
import platformConnect as pc
import os
from flask import make_response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gif')
def send_gif():
    query = request.args.get('query')
    number = request.args.get('number')
    result=ac.connectGiphy(query,number)
    result= fr.makeImageResponse(result)
    #result = pc.makeCfResponse(result)
    result = json.dumps(result, indent=4)
    result= make_response(result)
    return result

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(debug=False, port=port, host='127.0.0.1')


