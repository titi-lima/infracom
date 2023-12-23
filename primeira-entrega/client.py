import socket

ip = '127.0.0.1'
port_server = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip, port_server)

msg = input("Digite uma mensagem:")
chunks = [msg[i:i+1024] for i in range(0, len(msg), 1024)]

for chunk in chunks:
    udp.sendto(bytes(chunk, "utf8"), dest)

udp.close()