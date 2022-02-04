import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]


# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
# [2, 1]


def solution(progresses, speeds):
    answer = []
    days = []

    # 걸리는 날짜 구하기
    for i in range(0, len(progresses)):
       days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 배포일 계산
    i = 0
    while i < len(days):
        cnt = 0
        for j in range(i, len(days)):
            if days[i] >= days[j]:
               cnt += 1
            else:
                break
        answer.append(cnt)
        i += cnt
    return answer

print(solution(progresses,speeds))