temp = {'Monday':62, 'Tuesday':73, 'Wednesday':75, 'Thursday':70, 'Friday':76, 'Saturday':63, 'Sunday':70}

def getTemp (temp) :
    sum_ = 0
    index = 0 
    for key in temp :
        val = temp[key]
        sum_ += val
        index += 1
    return sum_ / index

def moderateDays (temp) :
    mod = list()
    for key in temp :
        val = temp[key]
        if 70 <= val <=79 :
            mod.append (key)
    return mod


name = ['John', 'Dana', 'Betty', 'Robby', 'John.']
age = [40, 35, 10, 8, 20]

def sortName (name, age) :
    d = dict (zip (name, age) )
    c = d.items ()
    b = list (c)
    b.sort ()
    print (b)


def most_frequent () :
    a = input ('input a string\n')
    d = dict ()
    lval = list ()
    lkey = list ()
    for ind in a :
        if ind != ' ' :
            d[ind] = d.get (ind, 0) + 1

def lettnum () :
    a = input ('enter a string of 7 letters\n')
    d = {'a':2, 'd':3, 'x':9, 'n':6, 'o':6, 'l':5}
    l = list ()
    for lett in a :
        if lett in d :
            s = str (d[lett])
            l.append (s)
    delimeter = ''
    c = delimeter.join(l)
    print (c)


odds = (9, 5, 11)
def tuplist (odds) :
    a = list (odds)
    a.sort()
    print (a)
    b = tuple (a)
    print (b)
