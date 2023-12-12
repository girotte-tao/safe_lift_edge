import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    while True:
        sio.send("Hello from client!")
        time.sleep(1)

@sio.event
def message(data):
    print('Received a message:', data)

@sio.event
def disconnect():
    print("I'm disconnected!")

if __name__ == '__main__':
    sio.connect('ws://127.0.0.1:5000')
    sio.wait()
