import socket

SERVER_IP = '192.168.122.129'
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))
filename = 'server1.jpg'
fp = open(filename, 'wb+')
count = 0

while True:
    data, addr = sock.recvfrom(1024)
    count += len(data)
    # buffer size 1024
    print("dikirim oleh [", addr, "] count: ",
          count, " panjang: ", len(data), data)
    fp.write(data)
