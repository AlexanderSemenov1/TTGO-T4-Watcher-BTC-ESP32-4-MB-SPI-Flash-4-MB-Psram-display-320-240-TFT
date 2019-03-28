import re

def __search__(r, s):  # ишет нужное значение в тексте
    match = re.search(r, s)  
    if match:
        match.group(0)
        return match.group(0)  # возврат результата
    return '            '

def __sub__(p, r, s): # удалить лишнее в найденом
    match = re.sub(p, r, s)
    if match:
        return match # возврат результата
    return '            '

def __points__(l):
    a= l[:6]
    b = list(a)
    c = str(b)
    d = c[2]+c[7]+'.'+c[12]+c[17]+'.'+c[22]+c[27]
    if d:
        return d
    return '            '
        
    # A - LAT - широта
    # N - LON - долгота
def latitude(self):  
    #"""latitude will return in the form str'xx.xxxxx'"""
    
    if self:
        L = __search__(r"(A\,\d\d\d\d\.\d+)", self)  # Ищет по букве А
        l = __sub__(r'(A),', '',  L)
        a= l[:2]; b= l[4:]
        c = a+b
        if c:
            return c
    return "No signal!"

def longitude(self):
    #"""longitude will return in the form str'xx.xxxxx'"""
    
    if self:
        L = __search__(r"(N\,\d\d\d\d\d\.\d+)", self)  # Ищет по букве N
        l = __sub__(r'N,0', '',  L)
        a= l[:2]; b= l[4:]
        c = a+b
        if c:
            return c
    return "No signal!"

def date(self):
    #"""Date will return in the form str'D.M.Y'"""
    
    if self:
        return "sorry unavailable"
    return "sorry unavailable"

def times(self):
    #"""Time will return in the form str'H.M'"""
    
    l = __search__(r"(\d\d\d\d\d\d\.00)", self)
    points = __points__(l)
    points = str(points)
    if points:
        return points
    return "No signal!"





