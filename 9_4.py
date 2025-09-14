fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)
senders = dict()
emails = list()

# Add email addresses to list
for x in handle :
    if not x.startswith('From ') : continue
    x = x.rstrip()
    emails.append(x.split()[1])

# Add email addresses to dictionary
for email in emails :
    senders[email] = senders.get(email, 0) + 1

# Find highest frequency sender
mailer = None
highcount = None
for x,y in senders.items() :
    if mailer is None or y > highcount :
        mailer = x
        highcount = y
        
print(mailer,highcount)