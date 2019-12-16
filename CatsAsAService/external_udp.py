import socket

# Send
SEND_UDP_IP = "127.0.0.1"
SEND_UDP_PORT = 5006
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receive
RECV_UDP_IP = "127.0.0.1"
RECV_UDP_PORT = 5007
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind((RECV_UDP_IP, RECV_UDP_PORT))

def test(datagrams):
    for datagram in datagrams:
        print("Sending datagram: {}".format(datagram))
        send_sock.sendto(datagram.encode(), (SEND_UDP_IP, SEND_UDP_PORT))
        data, _ = recv_sock.recvfrom(1024)
        print(data.decode("utf-8"))

print("---------- TEST 1 --------------")
datagrams = ["@Al~0", "ex - M~1", "ilk~"]
test(datagrams)

print("---------- TEST 2 --------------")
datagrams = ["@Dima~0", "sik - Mar~1", "tini~"]
test(datagrams)

print("---------- TEST 3 --------------")
datagrams = ["@Lap~0", "nik - Mea~1", "t~"]
test(datagrams)

print("---------- TEST 4 --------------")
datagrams = ["@Anime~0", "- Fish~"]
test(datagrams)


