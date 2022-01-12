import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "#DISCONNECT#"
GETSTATE_MESSAGE = "#GETSTATE#"
SETSTATE_MESSAGE = "#SETSTATE#"
ENDSETSTATE_MESSAGE = "#ENDSETSTATE#"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

positions = [[0, 0], [0, 0], [0, 0]]

def send(conn, msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	conn.send(send_length)
	conn.send(message)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	threadID = threading.activeCount() - 1

	setting_state = -1 # < 0 - not setting positions. > 0 setting positions

	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			if setting_state < 0:
				if msg == DISCONNECT_MESSAGE:
					connected = False
				elif msg == GETSTATE_MESSAGE:
					try:
						send(conn, str(positions[ (threadID+1) % 2 ][0]))
						send(conn, str(positions[ (threadID+1) % 2 ][1]))
					except:
						send(conn, str(positions[threadID][0]))
						send(conn, str(positions[threadID][1]))
				elif msg == SETSTATE_MESSAGE:
					setting_state = 0
			else:
				if msg == ENDSETSTATE_MESSAGE:
					setting_state = -1
				else:
					positions[threadID][setting_state] = int(float(msg))
					setting_state+=1


			print(f"[{addr}] {msg}")

	conn.close()

def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {PORT}")
	alive = True
	while alive:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
