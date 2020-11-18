while True:
    a = input ('Enter a integer between 0 and 100\n')
    if a.isdigit () :
        int (a)
        if '0' < a <= '100' :
            for num in range (a) :
                sum = sum + num
            print (sum)
            break
    else :
        print ('Invalid number')
