# Multiples of 3 or 5

max_range = 1000
my_list = [i for i in range (1,max_range) if i % 3 == 0 or i % 5 == 0]
sum = 0
for i in my_list:
    sum += i
print (sum)
