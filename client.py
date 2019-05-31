import socket

def client_program():
    host = socket.gethostname()
    port = 9500

    client_socket = socket.socket()
    client_socket.connect((host, port))

    msg = input(" -> ")

    while msg.lower().strip() != 'bye':
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: '+ data)

        msg = input(" -> ")
    
    client_socket.close()

if __name__ == '__main__':
    client_program()

