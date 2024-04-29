max = 1000000

sum = 0
for i in range(1,max):
    if str(i) == str(i)[::-1]:
        if str(bin(i)).lstrip("0b") == str(bin(i).lstrip("0b")[::-1]):
            sum += i

print (sum)

