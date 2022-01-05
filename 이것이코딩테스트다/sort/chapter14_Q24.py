import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

print(data[(N - 1) // 2])

# import sys
#
# N = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# I_min = int(1e9)
#
# # 집의 위치
# for x in data: # O(N)
#     I_cnt = 0
#     # 안테나 설치
#     for i in data: # O(N)
#         I_cnt += abs(i - x)
#
#     if I_min > I_cnt:
#         I_min = I_cnt
#         anthena = x
# print(anthena)