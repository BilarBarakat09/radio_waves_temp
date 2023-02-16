#receiver
from microbit import *
import radio
radio.config(group=13)
radio.on()
while True:
    message = radio.receive()
    if message =='hot':
        diplay.scroll(message)
    elif message =='cold':
        display.scroll(message)
