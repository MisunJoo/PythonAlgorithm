def solution(s):
    return changeWord(s.lower())

def changeWord(answer):
    dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                  'zero': 0}
    for key in dictionary.keys():
        if answer.find(key) != -1:
            answer = answer.replace(key, str(dictionary[key]))
    return int(answer)
