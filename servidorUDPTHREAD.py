from socket import *
import threading



class servidor():

    __serverPort = 12000
    def __init__(self) -> None:
        self.__serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.__serverSocket.bind(("", self.__serverPort))
        print("Chat iniciado, el servidor está listo para recibir")
        self.__clientAddress1=None
        self.__clientAddress2=None
        while self.__clientAddress2==None:
            if (self.__clientAddress1==None):
                message, self.__clientAddress1 = self.__serverSocket.recvfrom(2048)
                self.__serverSocket.sendto("cliente 1".encode(),self.__clientAddress1)
                print("cliente 1 asignado")
            elif (self.__clientAddress2==None):
                message, self.__clientAddress2 = self.__serverSocket.recvfrom(2048)
                self.__serverSocket.sendto("cliente 2".encode(),self.__clientAddress2)
                self.__serverSocket.sendto("cliente 2 asignado".encode(),self.__clientAddress1)
                print("cliente 2 asignado")

    def escucharClientes(self):
        message, clientAddress = self.__serverSocket.recvfrom(2048)
        while message!="adios":
            destino = self.__clientAddress2 if clientAddress==self.__clientAddress1 else self.__clientAddress1
            self.__serverSocket.sendto(message,destino)
            message, clientAddress = self.__serverSocket.recvfrom(2048)


        self.__serverSocket.close()



if __name__=="__main__":
    a=servidor()
    a.escucharClientes()




        

