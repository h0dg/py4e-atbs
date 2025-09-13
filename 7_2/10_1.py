fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
lst = list()
for line in fh :
    if not line.startswith('From ') : continue
    timestamp = line.split()[5]
    hour = timestamp.split(':')[0]
    lst.append(hour)
dct = dict()
for index in lst :
    dct[index] = dct.get(index, 0) + 1
tups = sorted(dct.items())
for (x,y) in tups :
    print(x,y)