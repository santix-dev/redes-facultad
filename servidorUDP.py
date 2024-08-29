from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("Chat iniciado, el servidor está listo para recibir")
clientAddress1=None
clientAddress2=None
while True:
    if (clientAddress1==None):
        message, clientAddress1 = serverSocket.recvfrom(2048)
        serverSocket.sendto("cliente 1".encode(),clientAddress1)
        print("cliente 1 asignado")
    elif (clientAddress2==None):
        message, clientAddress2 = serverSocket.recvfrom(2048)
        serverSocket.sendto("cliente 2".encode(),clientAddress2)
        serverSocket.sendto("cliente 2 asignado".encode(),clientAddress1)
        print("cliente 2 asignado")
    if (clientAddress1!=None and clientAddress2!=None):
        message, clientAddress = serverSocket.recvfrom(2048)
        destino = clientAddress2 if clientAddress==clientAddress1 else clientAddress1
        serverSocket.sendto(message,destino)




        

