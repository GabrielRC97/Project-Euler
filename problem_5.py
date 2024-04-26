# Smallest Multiple

max = 20
contador = max
result = 0

while result == 0:
    for i in range (1,max + 1):
        if contador % i != 0:
            contador += max
            break
        if i == max and contador % i == 0:
            result = contador

print (result)

