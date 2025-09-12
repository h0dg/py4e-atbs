fname = input('Enter file name: ')
#fname = 'mbox-short.txt'
try : fh = open(fname)
except :
    print('Could not open file:', fname)
    quit()
addresses = list()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    addresses.append(words[1])
    print(words[1])
print('There were', len(addresses), 'lines in the file with From as the first word')