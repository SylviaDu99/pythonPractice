def score () :
    n = input ('Enter score between 0.0 and 1.0\n')
    if ('0.0' <= n <= '1.0') :
        if ('0.9' <= n <= '1.0') :
            print ('A')
        elif ('0.8' <= n < '0.9') :
            print ('B')
        elif ('0.7' <= n < '0.8') :
            print ('C')
        elif ('0.6' <= n < '0.7') :
            print ('D')
        elif ('0.0' <= n < '0.6') :
            print ('F')
        score ()
    else :
        print ('Invalid Score')
        score ()

score ()
