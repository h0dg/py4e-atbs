#import re

#file = open('regex_sum_2294092.txt')
#nums = list()
#for line in file :
#    tmp = re.findall('[0-9]+', line)
#    if len(tmp) == 0 : 
#        continue    # skip lines without numbers
#    for num in tmp :
#        num = int(num) # convert to integer
#        nums.append(num)

#print(sum(nums))

import re
print(sum([int(x) for x in re.findall('[0-9]+', open('regex_sum_2294092.txt').read())]))

# 1. open('filename.txt').read()
#   - opens the file and reads the file into a single string.
#
# 2. re.findall('[0-9]+', ... ) where '...' is text to search
# 
# 3. [int(x) for x in ...]
#   - loops through each x in the list of regex matches.
#   - int(x) converts the string to an integer.

# LIST COMPREHENSION:
# [EXPRESSION for ITEM in ITERABLE]