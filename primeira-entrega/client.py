import socket

ip = '127.0.0.1'
port_server = 5000
buffer_size = 1024
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip, port_server)

filename = input("Enter filename:")
filename_ext = filename.split('.')[1] or ''
if filename_ext:
    filename_ext = '.' + filename_ext

with open(filename, 'rb') as f:
    while True:
        bytes_read = f.read(buffer_size)
        if not bytes_read:
            break
        udp.sendto(bytes_read, dest)

udp.sendto(b'FILE_TRANSFER_COMPLETE', dest)

# Receive the file from the server
with open('received_back_file'+filename_ext, 'wb') as f:
    while True:
        bytes_read, addr = udp.recvfrom(buffer_size)
        if bytes_read == b'FILE_TRANSFER_COMPLETE':
            break
        f.write(bytes_read)

print("File received back.")

udp.close()