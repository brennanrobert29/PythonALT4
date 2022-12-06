
import serial
import time


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM13"
ser.open()


while True:
    
 
microbitdata = str(ser.readline())
    

   steps = microbitdata[2:]
   steps = temperature.replace(" ","")
   steps = temperature.replace("\\r\\n","")
   steps = temperature.replace("'","")
   steps = int(steps)

    
    print("The distance you have completed", kilometeres)
    

    time.sleep(5)


ser.close()