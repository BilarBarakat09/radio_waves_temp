#sender
from microbit import *
import radio
radio.config(group=13)
radio.on()
temp = temperature()
while True :
    if temp >= 24:
        radio.send('hot')
    elif temp <=23:
        radio.send('cold')


