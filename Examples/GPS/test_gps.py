import machine, time
import gps

uart = machine.UART(2, 9600)
time.sleep(1)


while True:
    
    mygps = uart.read()
    mygps = str(mygps)
    
    time.sleep(0.3)
    
    print(gps.latitude(mygps), ' ', gps.longitude(mygps), ' ', gps.times(mygps))
    
    

 