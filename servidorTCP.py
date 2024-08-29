from socket import * 

import threading
class server:

    __serverPort = 12000
    __serverSocket = socket(AF_INET,SOCK_STREAM)
    
    __serverSocket.listen(2)
    __connectionSocket1 = None
    __connectionSocket2 = None
    __conexiones=[]
    __cliente = 1

    def __init__(self):
        self.__serverSocket.bind(('',self.__serverPort))
        print('Chat iniciado, el servidor está listo para recibir')
        while True:
            # hilo abajo
            self.escuchar()
            
            if (self.__connectionSocket1!=None and self.__connectionSocket2!=None):
                
                if cliente == 1:
                    message = self.__connectionSocket1.recv(2048).decode()
                    self.__connectionSocket2.send(message.encode())
                    cliente = 2
                if cliente == 2:
                    message = self.__connectionSocket2.recv(2048).decode()
                    self.__connectionSocket1.send(message.encode())
                    cliente = 1
    def escuchar(self):
        while True:
            socke, addr = self.__serverSocket.accept()
            socke.escuchar()
            threading.Thread(target=socke.escuchar)
            self.__conexiones.append(socke)

            # if (self.__connectionSocket1 ==None):
            #     self.__connectionSocket1, addr1 = self.__serverSocket.accept()
            #     self.__connectionSocket1.send("cliente 1".encode())
            #     print("cliente 1 asignado")
            # elif (self.__connectionSocket2==None):
            #     self.__connectionSocket2, addr2 = self.__serverSocket.accept()
            #     self.__connectionSocket2.send("cliente 2".encode())
            #     self.__connectionSocket1.send("cliente 2 asignado".encode())
            #     print("cliente 2 asignado")

class socke():
    __cliente=None
    def __init__(self,sock):
        self.__cliente=sock
    def escuchar(self):
        while True:
            message = self.sock.recv(2048).decode()
                    self.__connectionSocket2.send(message.encode())
                    cliente = 2

        
