import sys

data = list(map(int, list(sys.stdin.readline().rstrip())))
data.sort(reverse=True)

answer = 1
for i in data:
    if  i > 1: # 1을 생각 못함 # 쉬워보여도 작은 예시를 넣어보는 것을 잊지말자
        answer *= i
    else:
        answer += i
print(answer)