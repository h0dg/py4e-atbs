fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
try : fhandle = open(fname)
except :
    print('Unable to open file:', fname)
    quit()
senders = list()
for line in fhandle :
    if not line.startswith('From ') : continue
    senders.append(line.split()[1])
dct = dict()
for name in senders :
    dct[name] = dct.get(name, 0) + 1
revlist = list()
for key , value in dct.items() :
    x = (value, key)
    revlist.append(x)
x,y = (sorted(revlist, reverse=True)[0])
print(y,x)