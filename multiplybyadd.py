def multiply (a, b) :
    if b > 0 :
        c = a
        a = a + c
        b = b - 1
        return c + multiply (c, b)
    elif b == 0 or a == 0 :
        return 0
    elif b < 0 and a > 0 :
        c = b
        b = b + b
        a = a - 1
        return c + multiply (a, c)
    elif b < 0 and a < 0 :
        b = -b
        a = -a
        c = b
        b = b + b
        a = a - 1
        return c + multiply (a, c)
