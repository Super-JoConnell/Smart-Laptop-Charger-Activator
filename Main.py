# Script To Automize Smart Switch For Laptop Charger

import requests
#going to import another module that gathers battery info etc but like it is so late and i am tired and need to go to bed and watch some 90s tv shoes like sabrina the teenage witch because i am sad

#Constants

headers = {
    'Content-Type': 'text/plain',
    'Accept': 'application/json',
}

#Functions 

def Switch_Off():
    data = 'OFF'
    response = requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)


def Switch_On():
    data = 'ON'
    response = requests.post('http://192.168.8.234:8080/rest/items/OnOffSwitch', headers=headers, data=data)


def Main():
    Switch_Off()
    Switch_On()

if __name__ == "__main__":
    Main()
