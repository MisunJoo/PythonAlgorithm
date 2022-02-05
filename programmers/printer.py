priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 1

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # 만약 첫번째 요소가 queue에 들어있는 어떤 값보다 작다면
        # 뒤로 보내기
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        # 만약 아니라면 "출력"해줄 것이니까 answer += 1
        # cur[0]이 location과 같다면 처음에 뽑으려던 값이니까 answer 출력
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution(priorities, location))