input1 = '4'
input2 = '1 3 5 7'

N = int(input1)
numbers = map(int, input2.split())
answer = 0

for i in numbers:
    if i == 1:
        continue
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
    if check:
        answer += 1

print(answer)