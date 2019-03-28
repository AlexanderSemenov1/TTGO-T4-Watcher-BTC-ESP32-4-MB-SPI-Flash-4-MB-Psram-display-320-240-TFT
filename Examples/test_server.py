import machine
import socket
import time


html='''<!DOCTYPE html>
<html>
<head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><meta charset="utf-8"><title>ESP32</title></head>
<center><h2>Пример сервера с кнопками взаимодействия с ESP</h2></center>
<center><h2>MicroPython ESP</h2></center>
<form>
<button name="LED" value='ON' type='submit'> LED ON </button>
<button name="LED" value='OFF' type='submit'> LED OFF </button>
<button name="LED1" value='ON' type='submit'> LED1 ON </button>
<button name="LED1" value='OFF' type='submit'> LED1 OFF </button>
<br><br>
'''
LED0 = machine.Pin(2,machine.Pin.OUT); LED0.value(0)
LED1 = machine.Pin(5,machine.Pin.OUT); LED1.value(0)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.15',80))  # Тут нужно указать нужный вам IP адрес устройства
s.listen(5)
while True:
    conn,addr=s.accept()
    print("GOT a connection from %s" % str(addr))
    request=conn.recv(1024)
    print("Content %s" % str(request))
    request=str(request)
    print(request)
    LEDON=request.find('/?LED=ON')
    LEDOFF=request.find('/?LED=OFF')
    LED1ON=request.find('/?LED1=ON')
    LED1OFF=request.find('/?LED1=OFF')
    print(LEDON, LEDOFF)
    print(LED1ON, LED1OFF)
    if(LEDON==6):
        LED0.value(1)
    if(LEDOFF==6):
        LED0.value(0)
    if(LED1ON==6):
        LED1.value(1)
    if(LED1OFF==6):
        LED1.value(0)
    response=html
    conn.send(response)
    conn.close()