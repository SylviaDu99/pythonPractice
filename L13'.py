def print_hist (h) :
    for c in h :
        print (c, h[c])

def histogram (word) :
    d = dict ()
    for c in word :
        d[c] = d.get (c, 0) + 1
    return d

def reverse_lookup (d, v) :
    for k in d :
        if d[k] == v :
            return k
        raise ValueError
    
def invert_dict (d) :
    inverse = dict ()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

known = {0:0, 1:1}
def fibonacci (n) :
    if n in known :
        return known[n]

    res = fibonacci (n-1) + fibonacci (n-2)
    known[n] = res
    return res

been_called = False
def example1 () :
    global been_called
    been_called = True

known1 = {0:0, 1:1}
def example2 () :
    known1[2] = 1

def example3 () :
    global known1
    known1 = dict ()
