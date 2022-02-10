import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(0, N):
    data.append(list(map(int, sys.stdin.readline().split())))

answer = 1
for i in range(0, N):
    if min(data[i]) > answer:
        answer = min(data[i])

print(answer)