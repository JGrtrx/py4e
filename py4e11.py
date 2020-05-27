# Regular Expressions
import re

file = open('regex_sum_373066.txt')
nums = 0

for line in file : 
    line = line.rstrip()
    nums = nums + sum(map(lambda x : int(x), re.findall('([0-9]+)', line)))
    
print(nums)
