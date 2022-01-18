import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(data) -1


while True:
    mid = (end + start) // 2
    if data[start] > data[end]:
        mid = -1
        break;

    if data[mid] == mid:
        break;

    # 왼쪽 서치
    if data[mid] > mid:
        end = mid - 1
    # 오른쪽 서치
    if data[mid] < mid:
        start = mid + 1

print(mid)