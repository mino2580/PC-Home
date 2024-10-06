
import serial
import time
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data

with serial.Serial(port='COM6', baudrate=9600, timeout=1) as arduino:

    while True:
        num = input("Enter a number: ")
        value = write_read(num + "\n")
        value = value.decode("utf-8")
        #print(type(value))
        print(value)
