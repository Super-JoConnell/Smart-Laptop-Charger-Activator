<<<<<<< HEAD
# Script To Automize Smart Switch For Laptop Charger

import requests
import psutil
import time
import sys
from playsound import playsound

#Constants

headers = {
    'Content-Type': 'text/plain',
    'Accept': 'application/json',
}

#Functions 

def forceoff():  #sometimes my smart switch internal relay sticks so this is to work it back and forth to unstick
    while True:
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        time.sleep(4)
        batt = psutil.sensors_battery()
        plugged = bool(batt.power_plugged)
        print('After 1st Force is Plugg ON: ',plugged)
        while plugged == True:
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            time.sleep(4)
            batt = psutil.sensors_battery()
            plugged = bool(batt.power_plugged)
            print('After 2nd Force is Plugg ON: ',plugged)
        if plugged == False:
            print('Successfully Forced OFF')
            break
def forceon():  #sometimes my smart switch internal relay sticks so this is to work it back and forth to unstick
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()

def Switch_Off():
    try:
        data = 'OFF'
        requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)
    except:
        playsound('SFX/internet.wav')
        print('Please Make Sure You Have Connected to the Internet and Your Curl Command Destination is Correct')

def Switch_On():
    try:
        data = 'ON'
        requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)
    except:
        playsound('SFX/internet.wav')
        print('Please Make Sure You Have Connected to the Internet and Your Curl Command Destination is Correct')

def loop():
    while True:
        Main()

def Main():
    batt = psutil.sensors_battery()
    plugged = bool(batt.power_plugged)
    perc = int(batt.percent)
    print('Battery Charging: ', plugged)
    print('Battery Percentage: ', perc)
    if perc >= 75:
        if perc >= 78 and plugged == True:
            playsound('SFX/highbat.wav')
            forceoff()
        else:
            Switch_Off()
    elif perc <= 65:
        if perc <= 62 and plugged == False:
            playsound('SFX/lowbat.wav')
            forceon()
        else:
            Switch_On()
    time.sleep(30)


if __name__ == "__main__":
    loop()
=======
# Script To Automize Smart Switch For Laptop Charger

import requests
import psutil
import time
import sys
from playsound import playsound
from pynput import keyboard

#Constants

headers = {
    'Content-Type': 'text/plain',
    'Accept': 'application/json',
}

# Global Variable

a = True # Used for loop break connected to Hotkey

#Functions 

def gmodeon():
    playsound('SFX/gamemode.wav')
    print('<ctrl>+<alt>+<g> pressed -- GameMode Now Active')
    Switch_On()
    global a
    a = False

def gmodeoff():
    playsound('SFX/normalmode.wav')
    print('<ctrl>+<alt>+<b> pressed -- Battery Saver Cycle Active')
    Switch_Off()
    time.sleep(5)
    global a
    a = True

def exita():
    print('<ctrl>+<alt>+<e> pressed -- Now Exiting in 5 Seconds Thanks')
    time.sleep(5)
    sys.exit() #somehow this doesn't work LOL

def forceoff():  #sometimes my smart switch internal relay sticks so this is to work it back and forth to unstick
    while True:
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        Switch_On()
        Switch_Off()
        time.sleep(4)
        batt = psutil.sensors_battery()
        plugged = bool(batt.power_plugged)
        print('After 1st Force is Plugg ON: ',plugged)
        while plugged == True:
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            Switch_On()
            Switch_Off()
            time.sleep(4)
            batt = psutil.sensors_battery()
            plugged = bool(batt.power_plugged)
            print('After 2nd Force is Plugg ON: ',plugged)
        if plugged == False:
            print('Successfully Forced OFF')
            break

def forceon():  #sometimes my smart switch internal relay sticks so this is to work it back and forth to unstick
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()
    Switch_Off()
    Switch_On()

def Switch_Off():
    try:
        data = 'OFF'
        requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)
    except:
        playsound('SFX/internet.wav')
        print('Please Make Sure You Have Connected to the Internet and Your Curl Command Destination is Correct')

def Switch_On():
    try:
        data = 'ON'
        requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)
    except:
        playsound('SFX/internet.wav')
        print('Please Make Sure You Have Connected to the Internet and Your Curl Command Destination is Correct')

def loop():
    while True:
        while a == True:
            Main()
        else:
            print('Game Moce Active ...')
            time.sleep(5)
        

def Main():
    batt = psutil.sensors_battery()
    plugged = bool(batt.power_plugged)
    perc = int(batt.percent)
    print('Battery Charging: ', plugged)
    print('Battery Percentage: ', perc)
    if perc >= 75:
        if perc >= 78 and plugged == True:
            playsound('SFX/highbat.wav')
            forceoff()
        else:
            Switch_Off()
    elif perc <= 65:
        if perc <= 62 and plugged == False:
            playsound('SFX/lowbat.wav')
            forceon()
        else:
            Switch_On()
    time.sleep(30)


#Hotkey

h = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+g': gmodeon,
        '<ctrl>+<alt>+b': gmodeoff,
        '<ctrl>+<alt>+e': exita})
h.start()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        print('Program Ended By <ctr>+c Thank you for using this awesome program')
    
>>>>>>> f2a44e88031caa12dc73b667633af1290f39714c
