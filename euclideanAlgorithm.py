def mdc(a = 0, b = 0):
    while(b != 0):
        r = a % b
        a, b = b, r        
    return a
