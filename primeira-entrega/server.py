import socket

ip = ''
port = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (ip, port)
udp.bind(server)

with open('received_file', 'wb') as f:
    while True:
        bytes_read, addr = udp.recvfrom(1024)
        if bytes_read == b'FILE_TRANSFER_COMPLETE':
            break
        f.write(bytes_read)

print("File received.")

# Send the file back to the client
with open('received_file', 'rb') as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        udp.sendto(bytes_read, addr)

udp.sendto(b'FILE_TRANSFER_COMPLETE', addr)

udp.close()