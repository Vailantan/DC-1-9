import socket 
from threading import Thread 

class ClientThread(Thread):      
    def __init__(self, ip, port, conn):         
        Thread.__init__(self) 
        self.ip = ip         
        self.port = port     
        self.conn = conn    
        print("[+] New server socket thread started for " + ip + ":" + str(port))     
    
    def run(self):         
        while True: 
            data = self.conn.recv(2048).decode()             
            print("Client " + self.ip + ":" + str(self.port) + " sent:", data)
            if data == 'exit': 
                break 
            MESSAGE = input("Multithreaded Python server: Enter Response from Server/Enter exit:")             
            self.conn.send(MESSAGE.encode())  # echo

def main():
    TCP_IP = '0.0.0.0' 
    TCP_PORT = 2004 
    BUFFER_SIZE = 20

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpServer.bind((TCP_IP, TCP_PORT)) 
    threads = [] 

    try:
        while True: 
            tcpServer.listen(4) 
            print("Multithreaded Python server: Waiting for connections from TCP clients…") 
            (conn, (ip, port)) = tcpServer.accept()     
            newthread = ClientThread(ip, port, conn) 
            newthread.start()     
            threads.append(newthread) 
    except Exception as e:
        print("An error occurred:", e)
    finally:
        for t in threads:     
            t.join()

if __name__ == "__main__":
    main()  
