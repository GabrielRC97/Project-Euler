# Factorial Digit Sum

import math

problem = math.factorial(100)
sumatoria = 0

for i in str(problem):
    sumatoria += int(i)

print (sumatoria)
