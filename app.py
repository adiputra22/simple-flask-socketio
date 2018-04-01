from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS IS SECRETKEY 1231412'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/kirim')
def kirim_data():
	socketio.emit('my_response', {'data': 'data 1'}, namespace='/app1')
	return ('', 204)

@socketio.on('data_dari_browser', namespace='/app1')
def menerima_data(json):
    print('menerima data json: ' + str(json))

if __name__ == '__main__':
	socketio.run(app)

