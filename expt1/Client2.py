import socket 

def main():
    host = socket.gethostname() 
    port = 2004 
    BUFFER_SIZE = 2000 

    try:
        tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpClientB.connect((host, port)) 

        while True:
            MESSAGE = input("tcpClientB: Enter message/ Enter exit:") 
            tcpClientB.send(MESSAGE.encode()) 
            if MESSAGE == 'exit':
                break
            data = tcpClientB.recv(BUFFER_SIZE).decode() 
            print("Client received data:", data) 

        tcpClientB.close() 
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
