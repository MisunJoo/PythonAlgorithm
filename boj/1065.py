import sys
import math

N = int(sys.stdin.readline())
S = list(str(N))
answer = 0

if len(S) == 1:
    answer += N - 1 + 1
elif len(S) == 2:
    answer += N - 1 + 1
else:
    answer += 99

    # 처음에 N보다 작은 한수의 개수를 구하려면 그 사이값을 모두 비교해 줘야 하는걸 생각 못함
    # 파이썬은 숫자를 인덱스로 가져올 수도 있음! i[1]
    for i in range(100, N+1):
        string = str(i)

        first = int(string[1]) - int(string[0])
        last = int(string[2]) - int(string[1])

        # 한쪽 방향만 생각하고 반대방향은 생각 못함
        one = int(string[0]) - int(string[1])
        two = int(string[1]) - int(string[2])

        if first == last or one == two:
            answer += 1

print(answer)
