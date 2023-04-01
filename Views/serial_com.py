import serial
import vlc
import time
ser = serial.Serial('COM3',115200,timeout=0.05)
if not ser.isOpen():
    ser.open()
time.sleep(1)
ser.write("test".encode())
ser.close()


