import sys
from queue import PriorityQueue

# 데이터입력
cnt = 0
N = int(sys.stdin.readline())
A_data = PriorityQueue(maxsize=N)
for i in range(N):
    A_data.put(int(sys.stdin.readline()))

if A_data.qsize() == 1:
    print(0)
else:
    while A_data.qsize() > 1:
        first_min = A_data.get()
        second_min = A_data.get()
        cnt += first_min + second_min
        A_data.put(first_min + second_min)
    print(cnt)

