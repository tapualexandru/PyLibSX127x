
How to install LibSx127x in python3

1) uninstall node.js (If you had nodejs already installed)
	
	`sudo apt-get remove nodejs`   


2) Download and extract file

Raspberry Pi Model A, B, B+ and Compute Module

	wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv6l.tar.gz
	tar -xvf node-v4.0.0-linux-armv6l.tar.gz 
	cd node-v4.0.0-linux-armv6l

Raspberry Pi 2 Model B

	wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv7l.tar.gz
	tar -xvf node-v4.0.0-linux-armv7l.tar.gz` 
	cd node-v4.0.0-linux-armv7l`

3) Move all to /usr/local/

	`sudo cp -R * /usr/local/`

4)And now feel free to check your current running version.

	node -v

5) Install node.js lib

	`npm install sx127x`

6)Run reciver.py or sender.py(python3 sender.py or python3 reciver.py)


Hardware Wiring


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





https://gist.github.com/jsdario/bc32a8d02b90e53bd1e6feb014797084
https://github.com/sandeepmistry/node-sx127x

