# TTGO-T4-Watcher-BTC-ESP32-4-MB-SPI-Flash-4-MB-Psram-display-320-240-TFT

Sources of information:
For the display:  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display
Firmware Info:    https://github.com/m5stack/M5Cloud#lcdpolyx-y-r-sides-thick-color-fillcolor-rotate

#Initializing the display, setting up a connection to the wifi network.
from m5stack import lcd, buttonA, buttonB, buttonC
import network
import utime
lcd.init(lcd.M5STACK, width=320, height=240, mosi=23, miso=12,  clk=18, cs=27, dc=26, rst_pin=5, invrot=0, bgr=True)
lcd.orient(3)

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("*********", "*******") # Connect to an AP
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
