import math
import sys

N, K = map(int, sys.stdin.readline().split())
number = N
answer = 0

while True:
    if number == 1:
        break

    if number % K != 0:
        number -= 1
        answer += 1
    else:
        number = number // K
        answer += 1

print(answer)