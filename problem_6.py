# Sum Square Difference

def sum_of_factor(n):
    suma = sum(list(map(lambda n:n**2,range(1,n+1))))
    return suma

def square_of_sum(n):
    suma = 0
    for i in range(0,n+1):
        suma += i
    return suma ** 2


valor = 100

print (square_of_sum(valor) - sum_of_factor(valor))