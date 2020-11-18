def root (a) :
    x = 1.0
    epsilon = 0.00000000000000000000000000000000001
    while True :
        y = (x + a / x) / 2
        if abs (y - x) < epsilon :
            break
        x = y
        print (x)

def addsum (n) :
    a = 0
    for i in range (n) :
        b = int (input ('enter a number') )
        if b <= 100 :
            a = a + b
        print (a)

#while True :
#    line = input ('>>> ')
#    if line [0] == '#' :
#        continue
#    if line == 'done' :
#        break
#    print (line)
#print ('Done!')



#largest = None
#print ('Before: ', largest)
#for itervar in [1, 2, 3, 4, 5]:
#    if largest is None or itervar > largest :
#        largest = itervar
    #print ('Loop: ', itervar, largest)
#print ('Largest:', largest)
