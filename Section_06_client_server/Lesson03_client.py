import socket

# add server settings as a tuple (ip, port)
server_address = ('localhost', 8080)
# client setup
client = socket.socket()
client.connect(server_address)
# sending data bytes
client.send(bytes("Hello Server", encoding="UTF-8"))  # str to bytes
# client.send(bytes("stop", encoding="UTF-8"))  # stop cmd for the Server if needed
# reading server response
data = client.recv(4096)
print(data.decode("UTF-8")) # decode bytes to str
# client.send(bytes("stop", encoding="UTF-8"))
