import socket

def main():
    host = socket.gethostname()
    port = 2004
    BUFFER_SIZE = 2000

    try:
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((host, port))
        
        while True:
            MESSAGE = input("tcpClientA: Enter message/ Enter exit:")
            tcpClientA.send(MESSAGE.encode())
            if MESSAGE == 'exit':
                break
            data = tcpClientA.recv(BUFFER_SIZE).decode()
            print("Client2 received data:", data)

        tcpClientA.close()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
