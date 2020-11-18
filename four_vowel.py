def four_vowel () :
    n = input ("Please enter anything\n")
    if type (n) == str :
        if len (n) >= 4 :
            four = n[3]
            if four == 'a' or four == 'e' or four == 'i' or four == 'o' or four == 'u' :
                return True
            elif four == 'A' or four == 'E' or four == 'I' or four == 'O' or four == 'U' :
                return True
            else :
                return False
        else :
            return False
    else :
        return False
