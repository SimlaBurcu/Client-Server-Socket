from socket import *
import sys

#Sinif listesini txt'den okuyup numaraya gore siraliyan kisim
classlist = []
with open('siniflistesi.txt') as f:
    for line in f:
        classlist.append(line)
classlist.sort() 

#Serverin olusturuldugu kisim
serverPort=int(sys.argv[1])#Portu arguman olarak aliyor
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
	connectionSocket,addr=serverSocket.accept()
	indexFromClient=connectionSocket.recv(1024).decode('utf-8')
	if not indexFromClient:#Client baglantiyi kapattiysa ilgili clientin baglantisini kapat(close ile) yeni client bekle(continue ile while'in sonraki iterasyonuna geciyor.)
		connectionSocket.close()
		continue
	element=classlist[int(indexFromClient)]#Verilen index'teki veriyi al
	connectionSocket.send(element.encode('utf-8'))
	connectionSocket.settimeout(30)#Bilgiyi gonderdikten sonra 30 degisiklik bekle
	try:
		indexFromClient2=connectionSocket.recv(1024).decode('utf-8')
		if not indexFromClient2:#Client baglantiyi kapattiysa 
			connectionSocket.close()
			continue
		changeFromClient2=connectionSocket.recv(1024).decode('utf-8')
		if not changeFromClient2:#Client baglantiyi kapattiysa 
			connectionSocket.close()
			continue
		classlist[int(indexFromClient2)]=changeFromClient2#Client'tan gelen degisikligi uygula
		connectionSocket.send(("Change is done successfully."+classlist[int(indexFromClient2)]).encode('utf-8'))
	except timeout:#30 sn dolunca kullaniciyi uyararak ilgili client'in baglantisini kapat
		print("\nServer time out.")
		print("Server closed the connection.")
		print("Press enter to close client connection.")
		
	connectionSocket.close()
