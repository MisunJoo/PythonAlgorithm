
n = int(input())
arr = [list(input()) for _ in range(n)]

def indexOfRange(k, l):
    if k < 0 or l < 0 or k >= n or l >= n:
        return False
    else:
        return True
def changeTopIndex(tmpArr, k, l):
    tmp = tmpArr[k][l]
    tmpArr[k][l] = tmpArr[k + 1][l]
    tmpArr[k + 1][l] = tmp
    return tmpArr

def chnageRightIndex(tmpArr, k, l):
    tmp = tmpArr[k][l]
    tmpArr[k][l] = tmpArr[k][l + 1]
    tmpArr[k][l + 1] = tmp
    return tmpArr
def checkCandyV2(tmpArr,a, b, direction):
    candy = 0

    K_range_left = a
    if direction == 'Right':
        K_range = a + 1

    elif direction == 'Top':
        K_range =  n

    for k in range(K_range_left, K_range):#range(b, b+2):
        Rightanswer = 1
        previousCandy = 'X'
        for h in range(n):
            if previousCandy == tmpArr[k][h]:
                Rightanswer += 1
            else:
                Rightanswer = 1
            previousCandy = tmpArr[k][h]
            if Rightanswer > candy:
                candy = Rightanswer

    H_range_left = b
    if direction == 'Right':
        H_range = n
    elif direction == 'Top':
        H_range = b + 1


    for h in range(H_range_left, H_range): #range(a, a+2):
        Topanswer = 1
        previousCandy = 'X'
        for k in range(n):
            if previousCandy == tmpArr[k][h]:
                Topanswer += 1
            else:
                Topanswer = 1
            previousCandy = tmpArr[k][h]

            if Topanswer > candy:
                candy = Topanswer
    return candy

def checkCandyAll(tmpArr):
    candy = 0
    for k in range(n):
        Rightanswer = 1
        previousCandy = 'X'
        for h in range(n):
            if previousCandy == tmpArr[k][h]:
                Rightanswer += 1
            else:
                Rightanswer = 1
            previousCandy = tmpArr[k][h]
            if Rightanswer > candy:
                candy = Rightanswer
    for h in range(n):
        Topanswer = 1
        previousCandy = 'X'
        for k in range(n):
            if previousCandy == tmpArr[k][h]:
                Topanswer += 1
            else:
                Topanswer = 1
            previousCandy = tmpArr[k][h]
            if Topanswer > candy:
                candy = Topanswer

    return candy

candy = checkCandyAll(arr)
# print(candy)
for i in range(n):
    for j in range(n):
        tmpArr1 = [item[:] for item in arr]
        if indexOfRange(i, j+1):
            resArr1 = chnageRightIndex(tmpArr1, i, j)
            answerRight = checkCandyV2(resArr1, i, j, 'Right')
            answerTop = checkCandyV2(resArr1, i, j, 'Right')
            answerCandy = max(answerRight, answerTop)
        tmpArr2 = [item[:] for item in arr]
        if indexOfRange(i+1, j):
            resArr2 = changeTopIndex(tmpArr2, i, j)
            answerRight2 = checkCandyV2(resArr2, i, j, 'Top') # Top 일때만 b+2
            answerTop2 = checkCandyV2(resArr2, i, j, 'Top')
            answerCandy2 = max(answerRight2, answerTop2)
        answerCandy = max(answerCandy2, answerCandy)

        if answerCandy > candy:
            candy = answerCandy
print(candy)