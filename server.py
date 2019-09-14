# -*- coding: utf-8 -*-

#note: "$ pip3 install eventlet" required

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

@app.route('/nex/<int:pagenum>')
def sendpage(pagenum, methods=['GET','POST']):
	socketio.emit('pgevent',{'page': pagenum})
	return pagenum

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('msgevent')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('evresponse', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port="5000", debug=True)