phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    answer = True
    data = list()

    phone_book.sort(reverse=True)

    for i in range(0, len(phone_book)):
        if i == len(phone_book) - 1:
            continue
        after = phone_book[i+1]
        if after == phone_book[i][0:len(after)]:
            answer = False
    return answer

print(solution(phone_book))


# def solution(phone_book):
#     answer = True
#
#     sorted(phone_book, key=len)
#     for i in range(0, len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i] == phone_book[j][0:3]:
#                 answer = False
#
#     return answer