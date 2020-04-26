#encoding:utf-8
#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO,emit,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/',methods=['get'])
def index():
    return render_template('index.html')



#接收前台消息，并广播出去
@socketio.on('request_for_response',namespace='/testnamespace')
def give_response(data):
    value = data.get('param')
    emit('response',{'code':'200','msg':'春江潮水连海平'})




if __name__ == '__main__':
    socketio.run(app,debug=True)