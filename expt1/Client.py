import socket

def client_program():
    host = socket.gethostname()
    port = 5000  # socket server port number
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    message = input("Enter message to send -> ")
    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Received from server:", data)
        message = input("Enter message to send -> ")

    client_socket.close()  # close the connection

if __name__ == "__main__":
    client_program()
