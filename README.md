# LibSx127x

LibSx127x is SX127x librari for python3 which makes it easier to comunicate using LoRa module



## How to install LibSx127x in python3

### 1) uninstall node.js (If you had nodejs already installed)
	
	`sudo apt-get remove nodejs`   


### 2) Download and extract file

#### Raspberry Pi Model A, B, B+ and Compute Module

	wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv6l.tar.gz
	tar -xvf node-v4.0.0-linux-armv6l.tar.gz 
	cd node-v4.0.0-linux-armv6l

#### Raspberry Pi 2 Model B

	wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv7l.tar.gz
	tar -xvf node-v4.0.0-linux-armv7l.tar.gz` 
	cd node-v4.0.0-linux-armv7l`

### 3) Move all to /usr/local/

	`sudo cp -R * /usr/local/`

### 4)And now feel free to check your current running version.

	node -v

### 5) Install node.js lib

	`npm install sx127x`



## Run reciver.py or sender.py
	
	python3 sender.py
	python3 reciver.py


## Hardware Wiring


| LoRa | RPi | 
|--------------------:|:--------------------|
| VCC | 3.3V |
| GND |  GND |
| SCK | GPIO11 |
| MISO | GPIO10 |
| MOSI | GPIO9 |
| NSS | GPIIO7 |
| NRESET | GPIO24 |
| DIO0 | GPIO25 |      


## API

### `setFrequency(string)`

This method set carrier frequency ex `setFrequency("868e6")`

### `send(string)`

This metrhod transmit string using the lora module

### `setReciveMod(function)` 

This method set LoRa on recive mode and call function with message and RSSI as parameters when message is recived.
!Atention this function contain a infinit loop

	def onRecive(message, RSSI):
		print(message, RSSI)

	setReciveMod(function) 
	
	
### `setReciveModNewThread(self, onReceiveFunction):`
This method set LoRa on recive mode, move infinit loop in new thread and call function with message and RSSI as parameters when message is recived.

	def onRecive(message, RSSI):
		print(message, RSSI)

	setReciveModNewThread(function) 



https://gist.github.com/jsdario/bc32a8d02b90e53bd1e6feb014797084
https://github.com/sandeepmistry/node-sx127x

