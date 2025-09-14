import re

file = open('regex_sum_2294092.txt')
nums = list()
for line in file :
    tmp = re.findall('[0-9]+', line)
    if len(tmp) == 0 : 
        continue    # skip lines without numbers
    for num in tmp :
        num = int(num) # convert to integer
        nums.append(num)

print(sum(nums))