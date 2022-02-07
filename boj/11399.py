import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

# 1
# 1+2
# 1+2+3

def sumUntil(arr, n):
    cnt = 0
    for i in range(0, n+1):
        cnt += arr[i]
    return cnt

final_cnt = 0
for i in range(0, N):
    final_cnt += sumUntil(data, i)

print(final_cnt)