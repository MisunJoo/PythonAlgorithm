import sys

inputStr = sys.stdin.readline()

index_one = 0
index_zero = 0
index_smaller = 0
oneCount = inputStr.count('1')
zeroCount = inputStr.count('0')

for i in range(0, len(inputStr)):
    if inputStr[i] == '1':
        if i < len(inputStr) - 1:
            if inputStr[i] != inputStr[i + 1]:
                index_one += 1
    if inputStr[i] == '0':
        if i < len(inputStr) - 1:
            if inputStr[i] != inputStr[i + 1]:
                index_zero += 1
    answer = min(index_one, index_zero)
print(answer)
