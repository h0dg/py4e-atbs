import re
#x = 'My favorite 2 numbers are 19 and 42.'
#y = re.findall('[0-9]+', x) # one or more digits
#y = re.findall('[AEIOU]+', x) # one or more uppercase vowels
#print(y)

# findall returns a list of all matches

text = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', text)
print(y)