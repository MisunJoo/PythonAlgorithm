# 시간초과 코드 (2021-12-28)
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N # 열외시킨 인덱스의 값
index = 0
finalAnswer = 0

def check(inputArr):
    for i in range(0, len(inputArr)):
        copyDP = inputArr[:]
        answer = 1

        del copyDP[i]
        maxNum = copyDP[0]

        for j in range(1, len(copyDP)):
            # print('arr[j]', copyDP[j])
            if copyDP[j] < maxNum:
                answer += 1
                maxNum = copyDP[j]
            else:
                break
        dp[i] = answer

    return dp.index(max(dp))

if len(set(arr)) == 1:
    finalAnswer = len(arr) - 1
    print(finalAnswer)
    exit()


while True:

    if sorted(arr, reverse=True) != arr:
        index = check(arr)
        del arr[index]
        finalAnswer += 1
    else:
        break


print(finalAnswer)
# 뒷부분


