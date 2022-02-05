
brown = 24
yellow = 24

import math

def solution(brown, yellow):
    answer = []
    square = brown + yellow

    for i in range(1, math.ceil(square / 2) + 1):
        if square % i != 0:
            continue
        for j in range(1, i+1):
            if square != i * j:
                continue
            if math.pow(j, 2) == square:
                answer.append((i,j))
            if math.pow(j, 2) < square < math.pow(i, 2):
                answer.append((i,j))

    # 놓친 부분
    # 조건에 노란색이 맞는지 체크
    for width, height in answer:
        if (width - 2) * (height - 2) == yellow:
            return [width, height]


print(solution(brown, yellow))