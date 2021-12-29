n = int(input())

ugly = [0] * n  # ugly 배열에는 i 번째 못생긴 수를 담음
ugly[0] = 1  # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
# 못생긴 수는 2, 3, 5의 배수인데 각각에 대해 몇 번 배수를 해줬는지를 세기위해 각각 인덱스를 둠
# i2는 2의 배수를 몇 번 곱했는지
# i3는 3의 배수를 몇 번 곱했는지
# i5는 5의 베수를 몇 번 곱했는지
# 초기에는 2, 3, 5를 0번 곱했으니 0을 대입
i2 = i3 = i5 = 0
# next2는 2의 배수의 어떤 값
# next3는 3의 배수의 어떤 값
# next5는 5의 배수의 어떤 값
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택 ( 오름 차순으로 나열할 것이기 때문)
    # 가장 작은 수를 선택해야 그 수에 곱을 해주면 다음으로 큰 수가 나오기 때문
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    # 그 중 가장 작은 수가 이전에 구해둔 2의 배수의 값과 같다면, 그 수를 늘려야 다음으로 큰 수가 나오므로 2 *그 수를 해야 함
if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5
print(ugly[n - 1])
