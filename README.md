# TTGO-T4-Watcher-BTC-ESP32-4-MB-SPI-Flash-4-MB-Psram-display-320-240-TFT

Sources of information:
For the display:  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display \n
Firmware Info:    https://github.com/m5stack/M5Cloud#lcdpolyx-y-r-sides-thick-color-fillcolor-rotate \n

#Initializing the display, setting up a connection to the wifi network.\n
from m5stack import lcd\n
lcd.init(lcd.M5STACK, width=320, height=240, mosi=23, miso=12,  clk=18, cs=27, dc=26, rst_pin=5, invrot=0, bgr=True)\n

