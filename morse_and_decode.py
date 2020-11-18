encode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
code = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..']

def morse () :
    c = dict (zip (encode, code))
    a = input ('enter the sentence\n')
    for key in a :
        if key == ' ' :
            print ('')
        elif key == '.' :
            print ('')
        else :
            print (c[key])

def decrypt () :
    c = dict (zip (code, encode))
    while True :
        a = input ('enter the message or enter done to exit\n')
        if a == 'done' :
            return
        else :
            print (c[a])

def main () :
    a = input ('code or decode?\n')
    if a == 'code' :
        morse ()
    elif a == 'decode' :
        decrypt ()
    else :
        print ('ERROR')

main ()
