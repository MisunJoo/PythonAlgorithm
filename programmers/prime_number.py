from itertools import permutations
import math

def solution(numbers):
    answer = 0
    visited = []

    # 나올 수 있는 수 모두 구함
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))  # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        # print(arr)
        for j in range(len(arr)):  # 생성한 list(arr) 길이만큼 for문 실행
            num = int(''.join(map(str, arr[j]))) # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            if num in visited:
                continue
            visited.append(num)
            if num == 1 or num == 0:
                continue
            if is_prime_number(num):
                answer += 1
    return answer

def is_prime_number(x):
    end = math.floor(math.sqrt(x)) # 에라토스테네스의 체를 이용해서 제곱근까지만 구해주면 됨
    chae = [False] * (end + 1)

    for i in range(2, end + 1):
        if x % i == 0:
            chae[i] = True
            return False
    return True