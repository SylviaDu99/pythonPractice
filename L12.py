def addall (x) :
	total = 0
	for q in x :
		total += q #total += q equal to total = total + q
	return total

#x = [15, 74, 3, 28]
#x.sort ()
#print (x)
#[3, 15, 28, 74]

def only_upper (t) :
    res = []
    for s in t :
        if s.isupper() :
            res.append (s)
    return res

numlist = list ()
while True :
    n = input ('Enter a number or enter done to show average\n')
    if n == 'done' :
        break
    n = float (n)
    numlist.append (n)

ave = sum (numlist) / len (numlist)
print (ave)
