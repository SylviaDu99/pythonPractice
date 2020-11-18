t = divmod (7, 3)
def min_max (t) :
    return min (t), max (t)

def print_all (*args) :
    print (args)

def sum_all (*args) :
    s = sum (args)
    print (s)

def hasMatch (t1, t2) :
    for x, y in zip (t1, t2) :
        if x == y :
            return True
    return False

#for index, element in enumerate ('abc') :
#    print (index, element)

#d = {'a':1, 'b':2, 'c':3}
#m = d.items()
#print (list (m))

#a = [('b', 2), ('a', 1), ('c', 3)]
#b = dict (a)
#print (b)

#c = dict (zip('abc', range (3) ))
#for key, val in c.items () :    #item create key and val tuples
#    print (val, key)

#txt = 'but soft what light in yonder window breaks'
#words = txt.split()
#t = list()
#for word in words :
#    t.append ((len(word), word))

#t.sort(reverse = True)  #descending

#res = list()
#for length, word in t:
#    res.append(word)

#print (res)


import random

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words :
    t.append ((len(word), random.random(), word))

t.sort(reverse = True)  #descending

res = list()
for length, _, word in t:
    res.append(word)

print (res)
