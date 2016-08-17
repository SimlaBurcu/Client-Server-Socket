from socket import *
import sys

#Sinif listesini txt'den okuyup numaraya gore siraliyan kisim
classlist = []
with open('siniflistesi.txt') as f:
    for line in f:
        classlist.append(line)
classlist.sort() 

#Serverin olusturuldugu kisim
while 1:
	serverPort=int(sys.argv[1]) #Portu arguman olarak aliyor
	serverSocket=socket(AF_INET,SOCK_DGRAM)
	serverSocket.bind(("",serverPort))
	print ("The server is ready to receive")
	indexFromClient,clientAddress=serverSocket.recvfrom(1024)
	if not indexFromClient:#Client baglantiyi kapattiysa ilgili clientin baglantisini kapat(close ile) yeni client bekle(continue ile while'in sonraki iterasyonuna geciyor.)
		connectionSocket.close()
		continue
	element=classlist[int(indexFromClient.decode('utf-8'))]#Verilen index'teki veriyi al
	serverSocket.sendto(element.encode('utf-8'),clientAddress)
	serverSocket.settimeout(30)#Bilgiyi gonderdikten sonra 30 degisiklik bekle
	try:
		indexFromClient2,clientAddress=serverSocket.recvfrom(1024)
		if not indexFromClient2:#Client baglantiyi kapattiysa 
			connectionSocket.close()
			continue
		changeFromClient2,clientAddress=serverSocket.recvfrom(1024)
		if not changeFromClient2:#Client baglantiyi kapattiysa 
			connectionSocket.close()
			continue
		classlist[int(indexFromClient2.decode('utf-8'))]=changeFromClient2.decode('utf-8')#Client'tan gelen degisikligi uygula
		serverSocket.sendto(("Change is done successfully."+classlist[int(indexFromClient2.decode('utf-8'))]).encode('utf-8'),clientAddress)
	except timeout:#30 sn dolunca kullaniciyi uyararak ilgili client'in baglantisini kapat
		print("\nServer time out.")
		print("Server closed the connection.")
		print("Press enter to close client connection.")
	serverSocket.close()

