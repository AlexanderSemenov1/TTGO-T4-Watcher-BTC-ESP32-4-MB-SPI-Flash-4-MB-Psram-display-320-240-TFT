# Пример работы многопоточного режима работы ESP32
import _thread, time
from machine import Pin

led2 = Pin(2, Pin.OUT, value=0)

def func1():
    n = 0
    while True:
        print('Function-1: {0:d}'.format(n))
        time.sleep(1)
        n += 1
        if n > 10:
            _thread.exit()
        
def LED():
    while True:
        led2.on()
        time.sleep(1)
        led2.off()
        time.sleep(1)
        


def func2():
    n = 0
    while True:
        print('Function-2: {0:d}'.format(n))
        time.sleep(2)
        n += 1
        if n > 10:
            _thread.exit()

p1 = _thread.start_new_thread(func1, [])  # Поток 1
    
p2 = _thread.start_new_thread(func2, [])  # Поток 2
   
p3 = _thread.start_new_thread(LED, [])    # Поток 3, мигает светодиод



