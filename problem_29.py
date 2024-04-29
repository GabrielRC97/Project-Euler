my_list = []

for i in range (2,101):
    for j in range (2,101):
        my_list.append(i ** j)

print (len(set(my_list)))