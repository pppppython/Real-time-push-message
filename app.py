'''
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/',methods=['get'])
def b():
    return render_template('b1.html')


@socketio.on('message')
def handle_message(message):
     send(message, namespace='/chat')
 
@socketio.on('my event')
def handle_my_custom_event(json):
      emit('my response', json, namespace='/chat')


if __name__ == '__main__':
    socketio.run(app)
'''

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
    print('收到前台消息:'+value)
    #进行一些对value的处理或者其他操作,在此期间可以随时会调用emit方法向前台发送消息
    emit('response',{'code':'200','msg':'春江潮水连海平'})




if __name__ == '__main__':
    socketio.run(app,debug=True)