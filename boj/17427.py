
input = '10'
A = int(input)
sum = 0

for i in range(1, A + 1):
    sum += (A // i) * i
print(sum)