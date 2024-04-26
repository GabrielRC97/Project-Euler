# 1000-digit Fibonacci Number

contador = 1
number_1 = 1
number_2 = 0
number_3 = 0
digit = 1000

while len(str(number_3)) < digit:
    number_3 = number_1 + number_2
    if number_1 > number_2:
        number_2 = number_3
        contador += 1
    else:
        number_1 = number_3
        contador += 1

print(number_3, contador)