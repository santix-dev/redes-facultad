from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message="1"
message = ("Soy cliente")
clientSocket.sendto(message.encode(),(serverName, serverPort))
respuesta, serverAddress = clientSocket.recvfrom(2048)
if (respuesta.decode())=="cliente 1":
    cliente=1
    respuesta, serverAddress = clientSocket.recvfrom(2048)
else:
    cliente=2

while message!="":
    if cliente==1:
        message = input("Tu: ")
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        cliente=2
    elif cliente==2:
        respuesta, serverAddress = clientSocket.recvfrom(2048)
        print("El: ",respuesta.decode())
        cliente=1
        
        
    
clientSocket.close()
