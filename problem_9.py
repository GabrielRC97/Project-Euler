# Special Pythagorean Triplet
import math

result = 1000

for i in range (1,result):
    for j in range (1,result):
        if i + j + math.sqrt(i*i+j*j) == result:
            factor_a = i
            factor_b = j
            factor_c = math.sqrt(i*i+j*j)


print(factor_a, factor_b)

print (factor_a * factor_b * factor_c)