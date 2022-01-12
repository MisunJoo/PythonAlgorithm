def solution(N, stages):
    answer = {}
    temp = len(stages) #스테이지에 도달한 플레이어의 수

    for i in range(1, N+1):
        if temp == 0:
            answer[i] = 0
        else:
            count = stages.count(i)
            answer[i] = count/temp
            temp -= count #놓친부분.
    return sorted(answer, key=lambda x:answer[x], reverse=True)