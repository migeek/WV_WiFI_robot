from socketio import Client

sio=Client()
sio.connect('http://192.168.1.93:5000')

username = "byvictorrr"
password = "calpoly"

# to connect the bot in a room
@sio.on("join room")
def join_room(msg):
	breakpoint()
	sio.emit("connect bot", data={'username': username, 'password':password})


@sio.on('message')
def on_message(msg):
	print(msg)


while True:
    msg = input("input message: ")
    sio.emit("robot message", {"message":msg, "username": username})

