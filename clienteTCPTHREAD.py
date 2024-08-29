from socket import * 
import threading
class cliente():
    __serverName = 'localhost'
    __serverPort = 12000
    __clientSocket = socket(AF_INET, SOCK_STREAM)
    __message = ("Soy cliente")
    

    def __init__(self):
        ip=input("ingrese ip: ")
        self.__serverName=ip
        self.__clientSocket.connect((self.__serverName,self.__serverPort))
        mensaje="o"
        while mensaje!="fin":
            mensaje = input("ingrese mensaje: ")
            self.__clientSocket.send(mensaje.encode())
            respuesta, serverAddress = self.__clientSocket.recvfrom(2048)
            print("servidor dice: ",respuesta.decode())
    
        # if (respuesta.decode())=="cliente 1":
        #     cliente=1
        #     respuesta, serverAddress = clientSocket.recvfrom(2048)
        # else:
        #     cliente=2

        # while message!="":
        #     if cliente==1:
        #         message = input("Tu: ")
        #         clientSocket.sendto(message.encode(),(serverName, serverPort))
        #         cliente=2
        #     elif cliente==2:
        #         respuesta, serverAddress = clientSocket.recvfrom(2048)
        #         print("El: ",respuesta.decode())
        #         cliente=1
        # clientSocket.close()
if __name__=="__main__":
    a=cliente()