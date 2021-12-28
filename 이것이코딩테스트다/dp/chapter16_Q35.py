# 1. 1 부터 1000까지의 dp 테이블 값을 구해놓기
n = int(input())
dp = [0] * 1000
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[5] = 5
answer = 0

for i in range(4, 1000):
    # 못생긴 수가 아닐 조건
    if i % dp[2] == 0:
        dp[i] = dp[i // dp [2]] * dp[2]
    elif i % dp[3] == 0:
        dp[i] = dp[i // dp[3]] * dp[3]
    elif i % dp[5] == 0:
        dp[i] = dp[i // dp[5]] * dp[5]

for i in range(1, 1000):
    if answer == n:
        answer = i - 1
        break
    if dp[i] == 0:
        continue
    else:
        answer += 1




