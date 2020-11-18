def nested_sqrt (a) :
    import math
    sum1 = 0
    sum2 = 0
    for num in a :
        if isinstance (num, int) :
            num = math.sqrt (num)
            sum1 += num
        else :
            for digit in num :
                digit = math.sqrt (digit)
                sum2 += digit
    return sum1 + sum2
