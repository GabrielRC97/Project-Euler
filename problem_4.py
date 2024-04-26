# Largest Palindrome Product

my_list = []

for i in range (1,1000):
    for j in range (1,1000):
        if str(i*j) == str(i*j)[::-1]:
            my_list.append(i*j)

max = 0
for i in my_list:
    if i > max:
        max = i

print(max)



