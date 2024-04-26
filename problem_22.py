# Names Scores

import string

characters = [i for i in string.ascii_uppercase]

file = open(r'Project Euler\Archivos\0022_names.txt')
my_string = file.read().replace('"','')
my_list = list(my_string.split(','))
file.close()

my_list.sort()

counter = 0
sumtotal = 0

for i in my_list:
    sum = 0
    for j in i:
        index = characters.index(j) + 1
        sum += index
    counter +=1   
    sum = sum * counter
    sumtotal += sum

print(sumtotal)
