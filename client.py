from socket import*
import sys
from threading import Thread

index=0#ilk index alimi
index2=0#degisiklik icin index alimi
change=""#kullanicidan degisiklik alimi
#Server'in ip ve portunu arguman olarak aliyor
serverName=sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:#Kullanicidan index girmesini bekle. Gecerli bir index girene kadar dongude kal, hicbir sey girmeden enter'a basarsa baglantiyi sonlandir.
	try:
		index=input("Input index:")
		if (index.isdigit() and int(index)<=45 and int(index)>0):
			break
		print("Error: Please enter a number between 1 and 45")
	except Exception as exception:
		clientSocket.close()
		sys.exit(0)
clientSocket.send(str(index).encode('utf-8'))
modifiedSentence=clientSocket.recv(1024).decode('utf-8')
print("From Server:",modifiedSentence)
#Kullanicidan degisiklik yapmak istedigi indexi ve degisikligi istenilen formatta al
while True:
	try:
		index2=input("Enter the index you want to change:")
		if (index2.isdigit() and int(index2)<=45 and int(index2)>0):
			break
		print("Error: Please enter a number between 1 and 45")
	except Exception as exception:
		clientSocket.close()
		sys.exit(0)
clientSocket.send(str(index2).encode('utf-8'))
while True:
	try:
		change=input("Enter change in format <Number>,<Name Surname>,<email>:")
		if len(change.rstrip())==0:
			raise Exception("Nothing entered")
		if change.count(",")!=2:
			print("Error: Please enter a valid change")
			continue
		inputlength=len(change)
		number,name,email=change[0:(inputlength-1)].split(",")
		if len(number)==9 and number.isdigit() and ("@" in email): #email veya isim girdisi ile ilgili daha cok kontrol yapilabilir. Odev metninde belirtilmedigi icin dogru formatta girildigi kabul edilmistir.
			break
		print("Error: Please enter a valid change")
	except Exception as exception:
		clientSocket.close()
		sys.exit(0)
clientSocket.send(str(change).encode('utf-8'))
answerFromServer=clientSocket.recv(1024).decode('utf-8')
print("From Server:",answerFromServer)
clientSocket.close()


