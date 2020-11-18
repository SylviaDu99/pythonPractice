n = input ('enter the number of integers\n')
n = int(n)
sum_ = 0
while n > 0 :
    m = input ('enter a number\n')
    m = int (m)
    if m <= 0 or m > 100 :
        n = n - 1
    else :
        sum_ += m
        n = n - 1
print (sum_)
