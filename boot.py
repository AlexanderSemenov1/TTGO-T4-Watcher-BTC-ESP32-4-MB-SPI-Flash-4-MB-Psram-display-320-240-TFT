from m5stack import lcd, buttonA, buttonB, buttonC
import network
import utime
lcd.init(lcd.M5STACK, width=320, height=240, mosi=23, miso=12,  clk=18, cs=27, dc=26, rst_pin=5, invrot=0, bgr=True)
lcd.orient(3)

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("RT-WiFi_FF68", "XDTRNYDT") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

#rez = str(sta_if.ifconfig())

if not sta_if.isconnected():
    sta_if.connect()
    print("Waiting for connection...")
    while not sta_if.isconnected():
        utime.sleep(1)

lcd.setCursor(0, 40)
lcd.setColor()
lcd.println(str(sta_if.ifconfig()))
#import test


