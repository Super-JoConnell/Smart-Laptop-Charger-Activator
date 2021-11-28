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
