from m5stack import lcd, buttonA, buttonB, buttonC
import micropython, machine, time

#def but_a():
#    lcd.clear(lcd.OLIVE)
#    lcd.setCursor(0, 0)
#    lcd.setColor(lcd.RED, lcd.OLIVE)  # Красный
#    lcd.line(0, 15, 100, 15, 0xFF00FF)
#    lcd.rect(75, 75, 50, 50, 0x0000FF, lcd.GREEN)
#    lcd.circle(100, 100, 50, 0xFF8000)
#    lcd.roundrect(160, 100, 80, 80, 10, lcd.BLACK) # Прямоугольник (горизонт, вертикаль, шир, выс, закругление углов, цвет, заливка)
    
# Изменение цвета экрана по нажатию кнопки, точное время если есть соединение с сетью

def clock():
    rtc = machine.RTC()
    print("Synchronize time from NTP server ...")
    lcd.println("Synchronize time from NTP server ...")
    rtc.ntp_sync(server="ru.pool.ntp.org", tz="CET-3CEST,M3.5.0,M10.5.0/3") # Часовой пояс меняется в CET-3CEST
    lcd.clear(lcd.BLUE)
    lcd.setColor(lcd.BLACK, lcd.BLUE)
    lcd.font(lcd.FONT_Comic, fixedwidth=True, dist=16, width=2)
    while True :
        d = time.strftime("%d-%m-%Y", time.localtime())
        t = time.strftime("%H:%M:%S", time.localtime())
        lcd.print(d, lcd.CENTER, 50)
        lcd.print(t, lcd.CENTER, 130)
        time.sleep(0.02)
        if buttonA.isPressed():
             break
        if buttonС.isPressed():
             break

def but_a():
    lcd.clear(lcd.GREEN)
    lcd.setCursor(100, 100)
    lcd.setColor(lcd.BLACK, lcd.GREEN)
    lcd.print('Hello')

def but_b():
   lcd.clear(lcd.ORANGE)
   lcd.setCursor(100, 100)
   lcd.setColor(lcd.BLACK, lcd.ORANGE)
   lcd.print('World')
   return()     

lcd.font(lcd.FONT_Comic)
but_a()
buttonA.wasPressed(but_a)
buttonB.wasPressed(clock)
buttonC.wasPressed(but_b)
#buttonA.releasedFor(1.2, may_meny_A)
