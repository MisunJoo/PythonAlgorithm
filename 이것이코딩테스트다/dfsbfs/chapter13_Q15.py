from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [-1] * (N + 1)
q = deque([X])
visited[X] = 0

while q:
    city = q.popleft()
    for next_city in graph[city]:
        if visited[next_city] == -1: # 이게 -1일 때만 방문하면, 1-3로 거리를 구한 후 2-3의 거리를 못구하는 것 아닌가?
            visited[next_city] = visited[city] + 1 # 모든 거리 길이가 1이기 때문에 다음 방문할 도시와의 거리가 현재 도시의 +1인
            q.append(next_city)
flag = 0
for i in range(N + 1):
    if visited[i] == K:
        print(i)
        flag = 1

if flag == 0:
    print("-1")