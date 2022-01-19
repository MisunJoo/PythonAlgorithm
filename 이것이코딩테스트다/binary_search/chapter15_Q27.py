import sys

input = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
N = input[0]
x = input[1]

left_start = 0
left_end = len(data) - 1

right_start = 0
right_end = len(data) - 1

right_mid = (right_start + right_end) //2
left_mid = (left_start + left_end) //2

while True:
    #print('left_mid', left_mid, 'right_mid', right_mid)
    # 항상 탈출하는 조건
    if data[right_start] > x or data[left_end] < x:
        break

    if data[right_mid] != x and data[left_mid] != x:
        break

    # 왼쪽
    if data[left_mid] == x:
        left_end = left_mid
        left_mid = (left_start + left_end) // 2

    # 오른쪽
    if data[right_mid] == x:
        right_start = right_mid
        right_mid = (right_start + right_end) // 2 + 1

print((right_mid - 1) - (left_mid + 1) + 1)