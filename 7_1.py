# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("Unable to open file:" , fname)
    quit()
for i in fh :
    i = i.rstrip()
    i = i.upper()
    print(i)