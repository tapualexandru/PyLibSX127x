from libSx127x.LoRa import LoRa
import time

lora= LoRa()
lora.setFrequency('868e6')


def onRecived(message, signal):
	print(message,signal)
	#lora.exitReciveMode()



#lora.setReciveModNewThread(onRecived)
lora.setReciveMod(onRecived)
