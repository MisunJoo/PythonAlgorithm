lottos = [1, 2, 3, 4, 5, 6]
win_nums = [38, 19, 20, 40, 15, 25]
result = [1, 6]

def solution(lottos, win_nums):
    answer = []
    rank = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7}

    # 개수가 0개 => 1등, 1개 => 2등, 2개 => 3등, 3개 => 4등, 4개 => 5, 5개, 6개 => 6
    # 최소 등수
    min = rank[len(list(set(win_nums) - set(lottos)))] #4 0이 다 틀릴 때 => 맞은 것의 개수는 둘의 차집합
    print(min)
    #최대 등수 : 최소 등수 + 0의 개수
    max = rank[list(rank.keys())[list(rank.values()).index(min)] - lottos.count(0)]

    if min == 7:
        min = 6
    if max == 7:
        max =6

    # print(max)
    return sorted([min, max])


print(solution(lottos, win_nums))