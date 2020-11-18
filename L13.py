word = 'brontosaurus'
d = dict ()
#for c in word:
#    if c not in d :
#        d[c] = 1
#    else :
#        d[c] = d[c] + 1
#print (d)


#for c in word :
#    d[c] = d.get (c, 0) + 1
#print (d)


counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
lst = list (counts.keys())
lst.sort()
for key in lst :
    print (key, counts[key])
