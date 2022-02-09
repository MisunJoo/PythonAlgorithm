N, M, K = map(int, input().split())
data = list(map(int, input().split()))


data.sort(reverse=True)

def solution():
    answer = 0
    cnt = 0
    while True:
        for j in range(0, K):
            if cnt == M:
                return answer
            answer += data[0]
            cnt += 1
        if cnt == M:
            return answer
        answer += data[1]
        cnt += 1

print(solution())
