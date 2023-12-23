import socket 

ip = '127.0.0.1'

port_server = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest = (ip, port_server)

msg = input("Digite uma mensagem:")

udp.sendto (bytes(msg,"utf8"), dest)

msg, client = udp.recvfrom(1024)

print ("Mensagem recebida:", msg, "De:", client)

udp.close()