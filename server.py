import socket

def server_program():
    host = socket.gethostname()
    port = 9500

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    c, a = server_socket.accept()
    print("Connection from: " + str(a))
    while True:
        data = c.recv(1024).decode()
        if data.lower() == 'hello':
            respond_Hi = "Hi"
            c.send(respond_Hi.encode())
            break
        if data.lower() != 'hello':
            respond_Goodbye = "Goodbye"
            c.send(respond_Goodbye.encode())
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        c.send(data.encode())

    c.close()
if __name__ == '__main__':
    server_program()