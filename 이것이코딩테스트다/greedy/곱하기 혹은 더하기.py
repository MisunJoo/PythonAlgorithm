import sys

data = list(map(int, list(sys.stdin.readline().rstrip())))
data.sort(reverse=True)

answer = 1
for i in data:
    if  i != 0:
        answer *= i
    else:
        answer += i
print(answer)