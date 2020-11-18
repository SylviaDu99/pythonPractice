sum_ = 0
count = 0
ave = 0
while True :
    n = input ('enter a number\n')
    if n.isdigit () :
        n = int (n)
        sum_ = sum_ + n
        count = count + 1
        ave = sum_ / count
    elif n == 'done' :
        print ('sum = ', sum_)
        print ('count = ', count)
        print ('average = ', ave)
        break
    else :
        print ('Invalid number')
