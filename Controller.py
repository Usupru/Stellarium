import math
import requests
import time
import bluetooth

sock = None
hc05_address = None

def find_hc05():
    global hc05_address
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True) 
    for addr, name in nearby_devices: 
        if "HC-05" in name:
            hc05_address = addr
            print(f"HC-05 found at address {hc05_address}")
            return addr
    print("HC-05 not found")
    return None

def connect_hc05():
    port = 1  
    global sock
    global hc05_address
    if hc05_address is None:
        print("No HC-05 address available.")
        return None

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try: 
        print(f"Attempting to connect to HC-05 at {hc05_address}...")
        sock.connect((hc05_address, port))
        print("Connection to HC-05 successful")
        return sock
    except bluetooth.btcommon.BluetoothError as e:
        print(f"Failed to connect: {e}")
        return None

def main():

    global sock

    print("Searching HC-05")
    find_hc05()

    if hc05_address:
        print("Connecting to HC-05")
        sock = connect_hc05()
    
        if sock is None:
            print("Error: Connection with HC-05 failed")
        else:
            print("Connection successful")
    else:
        print("No HC-05 device found. Retrying in 5 seconds...")
        time.sleep(5)
        main()


def send(sock, azu):
    sock.send(azu)

updateTime = 1
verbose = True

try:
    url = "http://localhost:8090/api/main/view"
    response = requests.get(url)
    data = response.json()
except:
    print("\nThe Stellarium software is closed, quitting!\n")
    exit()

main()

while True:
    verbose = input("Do you want to constantly show data in the terminal? (yes/no) ")
    try:
        verbose = str(verbose)
        if verbose.lower() == "yes":
            verbose = True
            break
        else:
            if verbose == "no":
                verbose = False
                break
            else:
                print("Error, please insert a valid value")
    except:
        print("Error, please insert a valid value")


while True:
    updateTime = input("Please enter the delay between serial communication ")
    try:
        updateTime = float(updateTime)
        break
    except:
        print("Error, please insert a valid value")


while True:
 
    try:
        url = "http://localhost:8090/api/main/view"
        response = requests.get(url)
        data = response.json()
    except:
        print("\nThe Stellarium software is closed, quitting!\n")
        exit()


    x, y, z = map(float, data["altAz"].strip("[]").split(","))

    azimut_rad = math.atan2(x, y)
    azimut_deg = math.degrees(azimut_rad)
    if azimut_deg < 0:
        azimut_deg += 360

    altitud_rad = math.asin(z)
    altitud_deg = math.degrees(altitud_rad)

    if verbose == True:
        print(f"Azimut: {azimut_deg:.2f}°")
        print(f"Altitud: {altitud_deg:.2f}°")

    mensaje = f"{azimut_deg:.2f};{altitud_deg:.2f}\n"
    send(sock, mensaje.encode('utf-8'))
    time.sleep(1)
