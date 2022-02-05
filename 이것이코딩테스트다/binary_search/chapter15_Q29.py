import sys

# 입력받기
input = list(map(int, sys.stdin.readline().split()))
N = input[0] # 집의 개수
C = input[1] # 공유기의 개수

data = list()
for i in range(0, N):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort()

# 시작점, 끝점, 중간점 구하기
start_idx = 0
end_idx = len(data) - 1
left_end = (start_idx + end_idx) // 2
right_start = (start_idx + end_idx) // 2
max_number = end_idx - start_idx
compare = 0
i = C - 1
# 중간점의 위치를 계쏙 바꿔가며, 최소거리가 더 작아지면 각각 방향으로의 탐색을 중단
while i >= 0:
    i -= 1
    print("left end", left_end, "start_idx", start_idx)
    print("end_idx", end_idx, "right start", right_start)
    min_left = left_end - start_idx
    min_right = end_idx - right_start

    minimum = min(min_left, min_right)
    print("minimum", minimum)
    print("max_number", max_number)
    if compare < minimum:
        compare = minimum
        left_end = (start_idx + left_end) // 2
        right_start = (right_start + end_idx) // 2
    else:
        break

print("compare", compare)
print(min(compare, max_number) + 1)