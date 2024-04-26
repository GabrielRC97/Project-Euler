# 10001st Prime


my_list = [2]
contador = 2
prime = 10001

while len(my_list) != prime:
    for i in my_list:
        if contador % i == 0:
            break
        if i == my_list[-1] and contador % i != 0:
            my_list.append(contador)
            break
    contador += 1

print (my_list[-1])






