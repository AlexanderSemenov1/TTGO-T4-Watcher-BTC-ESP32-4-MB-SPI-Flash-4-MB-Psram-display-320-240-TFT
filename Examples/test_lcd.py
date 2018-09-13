from m5stack import lcd
import machine, time, math

lcd.init(lcd.M5STACK, width=320, height=240, mosi=23, miso=12,  clk=18, cs=27, dc=26, rst_pin=5, invrot=0, bgr=True)
lcd.orient(3)

maxx = 240
maxy = 320
miny = 12

# fonts used in this demo
fontnames = (lcd.FONT_Default, lcd.FONT_7seg, lcd.FONT_Ubuntu, lcd.FONT_Comic, lcd.FONT_Tooney, lcd.FONT_Minya)

# print display header
#----------------------
def header(tx, setclip):
    # adjust screen dimensions (depends on used display and orientation)
    global maxx, maxy, miny

    maxx, maxy = lcd.screensize()
    lcd.clear()
    if maxx < 240:
        lcd.font(lcd.FONT_Small, rotate=0)
    else:
        lcd.font(lcd.FONT_Default, rotate=0)
    _,miny = lcd.fontSize()
    miny += 5
    lcd.rect(0, 0, maxx-1, miny-1, lcd.OLIVE, lcd.DARKGREY)
    lcd.text(lcd.CENTER, 2, tx, lcd.CYAN, transparent=True)

    if setclip:
        lcd.setwin(0, miny, maxx, maxy)

# Display some fonts
#-------------------
def dispFont(sec=5):
    header("DISPLAY FONTS", False)

    if maxx < 240:
        tx = "MicroPython"
    else:
        tx = "Hi from MicroPython"
    starty = miny + 4

    n = time.time() + sec
    while time.time() < n:
        y = starty
        x = 0
        i = 0
        while y < maxy:
            if i == 0: 
                x = 0
            elif i == 1:
                x = lcd.CENTER
            elif i == 2:
                x = lcd.RIGHT
            i = i + 1
            if i > 2:
                i = 0
            
            for font in fontnames:
                if font == lcd.FONT_7seg:
                    lcd.font(font)
                    lcd.text(x,y,"-12.45/",machine.random(0xFFFFFF))
                else:
                    lcd.font(font)
                    lcd.text(x,y,tx, machine.random(0xFFFFFF))
                _,fsz = lcd.fontSize()
                y = y + 2 + fsz
                if y > (maxy-fsz):
                    y = maxy
        


# Display random fonts
#------------------------------
def fontDemo(sec=5, rot=False):
    tx = "FONTS"
    if rot:
        tx = "ROTATED " + tx
    header(tx, True)

    tx = "ESP32-MicrpPython"
    n = time.time() + sec
    while time.time() < n:
        frot = 0
        if rot:
            frot = math.floor(machine.random(359)/5)*5
        for font in fontnames:
            if (not rot) or (font != lcd.FONT_7seg):
                x = machine.random(maxx-8)
                if font != lcd.FONT_7seg:
                    lcd.font(font, rotate=frot)
                    _,fsz = lcd.fontSize()
                    y = machine.random(miny, maxy-fsz)
                    lcd.text(x,y,tx, machine.random(0xFFFFFF))
                else:
                    l = machine.random(6,12)
                    w = machine.random(1,l // 3)
                    lcd.font(font, rotate=frot, dist=l, width=w)
                    _,fsz = lcd.fontSize()
                    y = machine.random(miny, maxy-fsz)
                    lcd.text(x,y,"-12.45/", machine.random(0xFFFFFF))
       
    lcd.resetwin()

# Display random lines
#-------------------
def lineDemo(sec=5):
    header("LINE DEMO", True)

    n = time.time() + sec
    while time.time() < n:
        x1 = machine.random(maxx-4)
        y1 = machine.random(miny, maxy-4)
        x2 = machine.random(maxx-1)
        y2 = machine.random(miny, maxy-1)
        color = machine.random(0xFFFFFF)
        lcd.line(x1,y1,x2,y2,color)
        
    lcd.resetwin()

# Display random circles
#----------------------------------
def circleDemo(sec=5,dofill=False):
    tx = "CIRCLE"
    if dofill:
        tx = "FILLED " + tx
    header(tx, True)

    n = time.time() + sec
    while time.time() < n:
        color = machine.random(0xFFFFFF)
        fill = machine.random(0xFFFFFF)
        x = machine.random(4, maxx-2)
        y = machine.random(miny+2, maxy-2)
        if x < y:
            r = machine.random(2, x)
        else:
            r = machine.random(2, y)
        if dofill:
            lcd.circle(x,y,r,color,fill)
        else:
            lcd.circle(x,y,r,color)
       
    lcd.resetwin()

#------------------
def circleSimple(sec=5):
    tx = "CIRCLE"
    header(tx, True)

    x = 110
    y = 160
    r = 110
    z = 0
    while z < 12:
        color = machine.random(0xFFFFFF)
        fill = machine.random(0xFFFFFF)
        lcd.circle(x,y,r,color,fill)
        r -= 10
        x += 10
        z += 1

# Display random ellipses
#-----------------------------------
def ellipseDemo(sec=5,dofill=False):
    tx = "ELLIPSE"
    if dofill:
        tx = "FILLED " + tx
    header(tx, True)

    n = time.time() + sec
    while time.time() < n:
        x = machine.random(4, maxx-2)
        y = machine.random(miny+2, maxy-2)
        if x < y:
            rx = machine.random(2, x)
        else:
            rx = machine.random(2, y)
        if x < y:
            ry = machine.random(2, x)
        else:
            ry = machine.random(2, y)
        color = machine.random(0xFFFFFF)
        if dofill:
            fill = machine.random(0xFFFFFF)
            lcd.ellipse(x,y,rx,ry,15, color,fill)
        else:
            lcd.ellipse(x,y,rx,ry,15,color)
        
    lcd.resetwin()

# Display random rectangles
#---------------------------------
def rectDemo(sec=5, dofill=False):
    tx = "RECTANGLE"
    if dofill:
        tx = "FILLED " + tx
    header(tx, True)

    n = time.time() + sec
    while time.time() < n:
        x = machine.random(4, maxx-2)
        y = machine.random(miny, maxy-2)
        w = machine.random(2, maxx-x)
        h = machine.random(2, maxy-y)
        color = machine.random(0xFFFFFF)
        if dofill:
            fill = machine.random(0xFFFFFF)
            lcd.rect(x,y,w,h,color,fill)
        else:
            lcd.rect(x,y,w,h,color)
        
    lcd.resetwin()

# Display random rounded rectangles
#--------------------------------------
def roundrectDemo(sec=5, dofill=False):
    tx = "ROUND RECT"
    if dofill:
        tx = "FILLED " + tx
    header(tx, True)

    n = time.time() + sec
    while time.time() < n:
        x = machine.random(2, maxx-18)
        y = machine.random(miny, maxy-18)
        w = machine.random(12, maxx-x)
        h = machine.random(12, maxy-y)
        if w > h:
            r = machine.random(2, h // 2)
        else:
            r = machine.random(2, w // 2)
        color = machine.random(0xFFFFFF)
        if dofill:
            fill = machine.random(0xFFFFFF)
            lcd.roundrect(x,y,w,h,r,color,fill)
        else:
            lcd.roundrect(x,y,w,h,r,color)
        
    lcd.resetwin()


dispFont()
fontDemo()
lineDemo()
circleDemo()
circleSimple()
ellipseDemo()
rectDemo()
roundrectDemo()