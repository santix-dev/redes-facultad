from socket import *
import threading

class cliente():

    __serverName = "localhost"
    __serverPort = 12000
    def __init__(self):
        ip=input("ingrese ip: ")
        self.__serverName=ip
        self.__clientSocket = socket(AF_INET, SOCK_DGRAM)
        message="1"
        # __message = ("Soy cliente")
        self.__clientSocket.sendto(message.encode(),(self.__serverName, self.__serverPort))
        respuesta, serverAddress = self.__clientSocket.recvfrom(2048)
        if (respuesta.decode())=="cliente 1":
            print("cliente 1")
            respuesta, serverAddress = self.__clientSocket.recvfrom(2048)
        else:
            print("cliente 2")

    def iniciar(self):
        self.__hiloEscucha=threading.Thread(target=self.escucha)
        self.__hiloHabla=threading.Thread(target=self.habla)
        self.__hiloEscucha.start()
        self.__hiloHabla.start()

    # def escucha(clientSocket):
    def escucha(self):
        respuesta, serverAddress = self.__clientSocket.recvfrom(2048)
        while respuesta!="adios":
            print("El: ",respuesta.decode(),"\n")
            respuesta, serverAddress = self.__clientSocket.recvfrom(2048)

    def habla(self):
        print("ya puedes hablar y recibir mensajes\n")
        message = input()
        while message!="adios":
            self.__clientSocket.sendto(message.encode(),(self.__serverName, self.__serverPort))
            message = input()
        self.__serverSocket.close()




if __name__=="__main__":
    a=cliente()
    a.iniciar()
    
        

  
