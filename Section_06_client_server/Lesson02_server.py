import socket

# add server settings as a tuple (ip, port)
server_address = ('', 8080)  # '' is any IP address of the computer
# server setup
server = socket.socket()
server.bind(server_address)
# number of clients in the queue
server.listen(3)  # 3 client only in the queue

print("waiting for clients ...")
# now get some bytes from incoming connection and do smth with it
while True:
    cli, accept = server.accept()  # accept() is a tuple with Client info and accept status
    data = cli.recv(4096)  # read 4096 bytes from pipe (string)
    print("Received from client:", data.decode("UTF-8"))
    # do smth with the data from Client
    # send feedback (ack) to Client (just testing)
    ackdata = "<ack>" + str(data)
    cli.send(bytes("ACK from Server", encoding="UTF-8"))
    # cli.close()

    if str(data.decode("UTF-8")) == "stop":
        print("Stopping server ...")
        cli.close()
        break



