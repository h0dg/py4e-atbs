fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('Unable to open file:' , fname)
    quit()
count = 0
total = 0

# two ways to do this. commented out one way.
for line in fh :
    #if not line.startswith('X-DSPAM-Confidence:') :
    if not 'X-DSPAM-Confidence:' in line :
        continue
    else :
        count = count + 1
        pos = line.find(':')
        num = float(line[pos + 1 : ])
        total = total + num
avg = total / count
print('Average spam confidence:' , avg)
#print(count)