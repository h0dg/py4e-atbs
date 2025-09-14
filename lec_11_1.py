import re # import regular expressions

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    #if line.startswith('From:') :
    #if re.search('^X.*:', line) :
    if  re.search('^X-\S+:', line) :
        print(line)