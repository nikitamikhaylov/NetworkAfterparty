import socket

# Has to be /var/www/html/index.html
LOG_FILE_PATH = "index.html"
FILE_ACCESS_RIGHTS = "a"

def logger(message):
    with open(LOG_FILE_PATH, FILE_ACCESS_RIGHTS) as log_file:
        log_file.write(message + '\n')

with open(LOG_FILE_PATH, "w+") as log_file:
    log_file.write("<pre>" + '\n')

allowed_food = ["Fish", "Meat", "Milk", "Bread", "Carrot", "Beer"]

def parse_message(message):
    print(message)
    author_and_food = message.split('-')
    author, food = author_and_food[0], author_and_food[1][:-1].strip()
    print(food)
    if food in allowed_food:
        logger("[SUCCESS] {}".format(author))
        return "Eaten by the Cat"
    else:
        return "ERROR"

# Send
SEND_UDP_IP = "127.0.0.1"
SEND_UDP_PORT = 5007
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receive
RECV_UDP_IP = "127.0.0.1"
RECV_UDP_PORT = 5006
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind((RECV_UDP_IP, RECV_UDP_PORT))

number_of_datagram_in_message = 0
current_message = ""

while True:
  data, _ = recv_sock.recvfrom(1024) # buffer size is 1024 bytes
  datagram = data.decode("utf-8")
  logger("[INFO] received datagram: {}".format(datagram))
  if datagram[-1] == "~":
      current_message += datagram
      logger("[INFO] Message: {}".format(current_message))
      return_message = parse_message(current_message).encode()
      current_message = ""
  else:
      current_message += datagram[:-2]
      return_message = "The Cat is amused by #{}".format(number_of_datagram_in_message).encode()
      number_of_datagram_in_message += 1
  send_sock.sendto(return_message, (SEND_UDP_IP, SEND_UDP_PORT))