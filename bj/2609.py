input = '24 18'
inputs = input.split()
A = int(inputs[0])
B = int(inputs[1])

min = 1
max = A * B

sorted(inputs)
if B % A == 0:
    min = A;
    max = B;
else :
    for i in range(1, A):
        if B % i == 0 and A % i == 0:
            min = i
    for i in range(1, A*B):
        if (i * B) % A == 0:
            max = i*B
            break;
print(min)
print(max)