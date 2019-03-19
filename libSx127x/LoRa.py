import subprocess, time, os, signal, threading


sendFile='libSx127x/LoRa_send.js'
reciveFile='libSx127x/LoRa_reciver.js'
nodeAddress='node'

class LoRa():
	def __init__(self):
		self.freq=0
		self.log=[]
		self.reciveMod=False
		self.loraInit=False
		

	def setFrequency(self , frequency):
		self.freq=frequency

	def send(self , message):
		self.exitReciveMode()
		comand = nodeAddress + " " + sendFile + " " + self.freq + " '" + message + "'"		
		self.sendProcess=subprocess.Popen(comand, stdout=subprocess.PIPE, shell=True)
	
		all_Line=[]
		for i in range(0,2):
			line = self.sendProcess.stdout.readline();
			decodeLine=line.decode("utf-8")
			decodeLine=decodeLine.replace('\n','')
			all_Line.append(decodeLine)
		self.sendProcess.kill()
		print(all_Line)


	def recive(self, packetNumber):
		self.exitReciveMode()
		comand = nodeAddress + " " + reciveFile + " " + self.freq
		self.reciveProcess=subprocess.Popen(comand, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		allDataReceived=[]
		for i in range(0,2*packetNumber+2):
			line = self.reciveProcess.stdout.readline();
			decodeLine=line.decode("utf-8")

			allDataReceived.append(decodeLine)
		self.reciveProcess.kill()
		print(allDataReceived)


	def setReciveMod(self, onReceiveFunction):
		self.exitReciveMode()
		self.reciveMode=True
		comand = nodeAddress + " " + reciveFile + " " + self.freq
		self.reciveProcess=subprocess.Popen(comand, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		allDataReceived=[]
		i=0
		line = self.reciveProcess.stdout.readline();
		decodeLine=line.decode("utf-8")

		if 'open success' in decodeLine:
			self.loraInit=True
		else:
			self.loraInit=False
			self.reciveMode=False
			print("Error to conect LoRa module")


		while self.reciveMode:
			line = self.reciveProcess.stdout.readline();
			decodeLine=line.decode("utf-8")
			decodeLine=decodeLine.replace("\n",' ')
			splitLine=decodeLine.split(";")
			threading.Thread(name="Reciv Thread", target=onReceiveFunction, args=[splitLine[0], splitLine[1]]).start()
			#onReceiveFunction(splitLine[0], splitLine[1])
	

	def setReciveModNewThread(self, onReceiveFunction):
                reciveThread = threading.Thread(name="Reciv Thread", target=self.setReciveMod, args=[onReceiveFunction])
                reciveThread.start()

	def exitReciveMode(self):
		try:
			self.reciveMode=False
			os.kill(self.reciveProcess.pid, signal.SIGKILL)
		except:
			pass
