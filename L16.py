import os
cwd = os.getcwd ()
print (cwd)

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile (path) :
            print(path)
        else :
            walk (path)

try:
    fin = open ('bad_file')
    for line in fin :
        print (line)
    fin.close()
except :
    print ('Something went wrong.')


def sed(pattern, replace, source, dest) :
    try:
        fin = open(source, 'r')  #r==read
        fout = open(dest, 'w')

        for line in fin :
            line = line.replace(pattern, replace)  # *.replace(a, b) == replace a into b in *
            fout.write (line)
            
        fin.close()    #auto save after close 
        fout.close()

    except :
        print ('something went wrong')


def main (name) :
    pattern = 'pattern'
    replace = 'replacendum'
    source = name
    dest = name + '.replaced.txt'
    sed (pattern, replace, source, dest)
