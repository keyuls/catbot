from flask import Flask
import apiConnect as ac
import facebookResponse as fr
import platformConnect as pc
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gif')
def send_gif():
    result=ac.connectGiphy()
    result= fr.makeImageResponse(result)
    result = pc.makeCfResponse(result)
    return result

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    # app.run(debug=False, port=port, host='0.0.0.0')
    app.run(debug=False, port=port, host='127.0.0.1')


