from libSx127x.LoRa import LoRa
import time

lora= LoRa()
lora.setFrequency('868e6')

i=0
while True:
	lora.send("Hello "+str(i))
	i+=1
