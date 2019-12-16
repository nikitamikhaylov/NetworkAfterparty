import socket

# create a socket object
send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server host and port
SERVER_TCP_IP = "127.0.0.1"
SERVER_TCP_PORT = 6008

def send_and_receive_message(message):
    # connection to hostname on the port.
    send_socket.connect((SERVER_TCP_IP, SERVER_TCP_PORT))
    print("Connected to server with TCP:{}".format(SERVER_TCP_PORT))
    print("Sending message: {}".format(message))
    send_socket.send(message.encode('ascii'))
    response = send_socket.recv(1024).decode('ascii')
    print("Received responce from the Cat: {}".format(response))
    send_socket.close()

message = "@Lapnik~@007~@Alex~@Lapnik~@Alex~@Anime~"
send_and_receive_message(message)

