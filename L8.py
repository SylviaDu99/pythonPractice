def factorial (n) :
    space = ' ' * (4 * n)
    print (space, 'factorial', n)
    if not isinstance (n, int) :
        print ('Invalid number')
        return None
    elif n == 0 :
        print (space, 'returning 1')
        return 1
    elif n < 0 :
        print ('Invalid number')
    else :
        recurse = factorial (n - 1)
        result = n * recurse
        print (space, 'returning', result)
        return result


def fibonacci (n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n < 0 :
        print ('Error')
    else :
        recurse = fibonacci (n - 1)
        recurse1 = fibonacci (n - 2)
        result = recurse1 + recurse
        return result
    

def ack (m, n) :
    if m == 0 :
        return n + 1
    elif n == 0 and m > 0 :
        result = ack (m - 1, 1)
        return result
    elif m > 0 and n > 0 :
        result = ack (m - 1, ack (m, n - 1) )
        return result
    else :
        print ('Invalid numbers')



n = 5
while n > 0 :
    print ('Stella')
    n = n - 1

