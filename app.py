import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5511933773729','+5511980320739']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'teste do programa',datetime.now().hour,datetime.now().minute + 2)
    del contatos[1]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')