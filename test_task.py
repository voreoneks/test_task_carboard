import serial
from gpiozero import CPUTemperature
from time import sleep
import subprocess
import json

if __name__ == '__main__':

    serialport = serial.Serial(port = '/dev/ttyAMA0', baudrate=9600, timeout=1.0, write_timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

    while True:
        temp = float(CPUTemperature().temperature)
        usbs = subprocess.check_output('lsusb') 
        usb_list = usbs.decode().split('\n')
        data_dict = {
            'CPU Temperature': temp,
            'USB Connections': usb_list}
        with open('data.json', 'w') as f:
            info_json = json.dump(data_dict, f)
        with open('data.json', 'r') as f:
            serialport.write(f.read().encode())
        sleep(1)


