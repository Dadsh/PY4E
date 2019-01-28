# The basic outline of this problem is to read the file, look for integers
# using the re.findall(), looking for a regular expression of '[0-9]+' and then
# converting the extracted strings to integers and summing up the integers.

handle = open('regex_sum_28259.txt')

import re

numlist = list()
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for item in numbers:
            num = int(item)
            numlist.append(num)
print(sum(numlist))
