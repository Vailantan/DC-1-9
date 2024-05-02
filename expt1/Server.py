import socket

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    print("Waiting for connection...")
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    
    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data_to_send = input("Enter message to send -> ")
        conn.send(data_to_send.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
