

input = '6'
input2 = '3 4 2 12 6 8'

N = int(input)
A = sorted(list(map(int, input2.split())))

print(A)

min = A[int(len(A)/2 -1)]
max = A[int(len(A)/2 )]

print(int(min*max))