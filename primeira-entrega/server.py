import socket 

ip = ''

port = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = (ip, port)

udp.bind(server)

msg, client = udp.recvfrom(1024)

print ("Mensagem recebida:", msg, "De:", client)

udp.sendto (msg, client)

udp.close()