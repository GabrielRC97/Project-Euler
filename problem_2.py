# Even Fibonacci Numbers

max_range = 4000000
my_list = []
valor_1 = 0
valor_2 = 1
for i in range(0, max_range):
    if i == valor_1 + valor_2:
        my_list.append(i)
        if valor_2 > valor_1:
            valor_1 = i
        else:
            valor_2 = i
            
print (my_list)

sum = 0

for i in my_list:
    if i % 2 == 0:
        sum += i
      
print (sum)