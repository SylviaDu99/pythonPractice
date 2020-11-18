import dbm
db = dbm.open ('captions.db', 'c')

db['cleese.png'] = 'photo of John Cleese'
#print (db['cleese.png'])

#for key in db :
#    print (key)

#db.close()

import pickle
t = [1, 2, 3]
s = pickle.dumps (t)
print (s)
t2 = pickle.loads (s)
print (t2)

t == t2
True #value same
t is t2
False #not same object

def linecount (filename) :
    count = 0
    for line in open (filename) :
        count += 1
    return count
print (linecount ('wc.py'))

#or can import wc
#wc.linecount ('wc.py')

if __name__ == '__main__' :   #__name__ : built-in variable, set as program start
    print (linecount('wc.py'))
