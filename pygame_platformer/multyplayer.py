import socket
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "10.100.102.129"
ADDR = (SERVER, PORT)

DISCONNECT_MESSAGE = "#DISCONNECT#"
GETSTATE_MESSAGE = "#GETSTATE#"
SETSTATE_MESSAGE = "#SETSTATE#"
ENDSETSTATE_MESSAGE = "#ENDSETSTATE#"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

pos = [0, 0]

otherPos = [0, 0]

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))

	client.send(send_length)
	client.send(message)

def recive(client):
	msg_length = client.recv(HEADER).decode(FORMAT)
	if msg_length:
		msg_length = int(msg_length)
		msg = client.recv(msg_length).decode(FORMAT)
	return msg

def loop(pos):
	send(SETSTATE_MESSAGE)

	send(str(pos[0]))
	send(str(pos[1]))

	send(ENDSETSTATE_MESSAGE)


	send(GETSTATE_MESSAGE)
	
	return int(recive(client)), int(recive(client))

def disconnect():
	send(DISCONNECT_MESSAGE)