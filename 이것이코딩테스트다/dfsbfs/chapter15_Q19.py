import sys
import itertools

answer_list = []
# 연산자 넣어a주기
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
symbols_input = list(map(int, sys.stdin.readline().split()))
symbols = list()
for i in range(0, symbols_input[2]):
    symbols.append('*');
for i in range(0, symbols_input[0]):
    symbols.append('+');
for i in range(0, symbols_input[1]):
    symbols.append('-');
for i in range(0, symbols_input[3]):
    symbols.append('/');
symbols = list(filter(lambda x: x != '', symbols))

# 순열 구하기
final_permutations = []
permutations = list(itertools.permutations(symbols))
for permutation in permutations:
    final_permutations.append(permutation)

# 식으로 합치기
for permutation in final_permutations:
    answer = numbers[0]
    for i in range(0, len(permutation)):
        if permutation[i] == '+':
            answer += numbers[i + 1]
        if permutation[i] == '-':
            answer -= numbers[i + 1]
        if permutation[i] == '*':
            answer *= numbers[i + 1]
        if permutation[i] == '/':
            if answer < 0:
                answer = -1 * ((-1) * answer // numbers[i + 1])
            else:
                answer //= numbers[i + 1]
    answer_list.append(answer)

print(max(answer_list))
print(min(answer_list))