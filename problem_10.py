# Summation of Primes


my_prime_number_list = []
max = 2000000
my_list =list(range(2,max + 1))

while len(my_list) != 0:
    my_prime_number_list.append(my_list[0])
    my_list = list(filter(lambda x: x % my_list[0] != 0, my_list))
       


print(sum(my_prime_number_list))
