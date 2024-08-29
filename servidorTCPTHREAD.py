from socket import * 
import threading

class servidor():
    __serverPort = 12000
    
    
    __connectionSocket1 = None
    # __connectionSocket2 = None
    __conexiones=[]

    def __init__(self):
        # ip=input("ingrese ip: ")
        self.__serverSocket = socket(AF_INET,SOCK_STREAM)
        self.__serverSocket.bind(('',self.__serverPort))
        self.__serverSocket.listen(2)

    def escucharConexion(self):
        while True:
            socke, addr = self.__serverSocket.accept()
            self.__conexiones.append(socke)
            hilo=threading.Thread(target=self.atender)
            hilo.start()
            # threading.Thread(target=socke.escuchar)
    def atender(self):
        numero=len(self.__conexiones)-1
        socke=self.__conexiones[numero]
        message="o"
        while message!="fin":
            message = socke.recv(2048).decode()
            socke.send(message.encode())
        socke.close()





if __name__=="__main__":
    a=servidor()
    # threading.Thread(target=a.escucharConexion)
    a.escucharConexion()