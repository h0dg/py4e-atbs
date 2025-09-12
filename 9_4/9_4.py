#fname = input('Enter file name: ')
fname = 'mbox-short.txt'
handle = open(fname)
senders = dict()
emails = list()
for line in handle :
    if not line.startswith('From ') : continue
    words = line.split()
    emails.append(words[1])
for email in emails :
    senders[email] = senders.get(email, 0) + 1

bigsender = None
sentcount = None
for key,value in senders.items() : # was missing .items()
    if bigsender == None :
        bigsender = key
        sentcount = value
    else :
        if value > sentcount :
            sentcount = value
            bigsender = key
print(bigsender,sentcount)