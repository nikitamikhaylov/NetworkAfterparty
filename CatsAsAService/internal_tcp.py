import socket

# Has to be /var/www/html/index.html
LOG_FILE_PATH = "index.html"
FILE_ACCESS_RIGHTS = "r"

def parse_message(message):
    authors = message.split("~")
    answer = []
    with open(LOG_FILE_PATH, FILE_ACCESS_RIGHTS) as log_file:
        log_file_lines = log_file.readlines()
        for author in authors:
            flag = False
            for line in log_file_lines:
                line = line.split()
                level, successor = line[0], line[1]
                if level == "[SUCCESS]" and author == successor:
                    flag = True
                    break
            answer.append(flag)
    assert(len(answer) == len(authors))
    return answer


# Receive
RECV_TCP_IP = "127.0.0.1"
RECV_TCP_PORT = 6008
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recv_sock.bind((RECV_TCP_IP, RECV_TCP_PORT))

# queue up to 5 requests
recv_sock.listen(5)

long_message = ""

while True:
    # establish a connection
    client_socket, addr = recv_sock.accept()
    print("Accepted connection")
    msg = client_socket.recv(1024).decode('ascii')
    print("Received message: {}".format(msg))
    answer = parse_message(msg)
    response = ""
    for ans in answer:
        if ans:
            response += "Tolerated by the Cat"
        else:
            response += "Scratched by the Cat"
    print("Sending response: {}".format(response))
    client_socket.send(response.encode('ascii'))
    client_socket.close()