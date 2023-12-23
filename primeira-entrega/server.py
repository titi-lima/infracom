import socket

ip = ''
port = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (ip, port)
udp.bind(server)

data = b''
while True:
    chunk, client = udp.recvfrom(1024)
    data += chunk
    if len(chunk) < 1024:
        break

print("Mensagem recebida:", data, "De:", client)

udp.close()