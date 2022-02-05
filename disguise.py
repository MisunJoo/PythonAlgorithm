clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    maxlen = 0
    data = {}

    for cloth in clothes:
        if cloth[1] in data:
            data[cloth[1]].append(cloth[0])
            if maxlen < len(data[cloth[1]]):
                maxlen = len(data[cloth[1]])
        else:
            data[cloth[1]] = [cloth[0]]
            if maxlen < len(data[cloth[1]]):
                maxlen = len(data[cloth[1]])

    for key in data.keys():
        answer = answer * (len(data[key]) + 1)
    return answer - 1

print(solution(clothes))
