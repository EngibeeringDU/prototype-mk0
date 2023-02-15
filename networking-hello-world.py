#Hello world over network between laptop and W5500 enabled RP2040

from usocket import socket
from machine import Pin,SPI
import network
import rp2
import time

led = Pin(25, Pin.OUT)

#W5x00 chip init
def w5x00_init():
    spi=SPI(1,2_000_000, mosi=Pin(11),miso=Pin(12),sck=Pin(10))
    nic = network.WIZNET5K(spi,Pin(13),Pin(15)) #spi,cs,reset pin
#     nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    nic.ifconfig(('10.0.0.4','255.255.255.0','10.0.0.1','8.8.8.8'))
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
        
def main():
    w5x00_init()
    
    while True:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

if __name__ == "__main__":
    main()