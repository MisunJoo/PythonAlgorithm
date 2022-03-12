import sys
from collections import deque
import time

N, L, R = map(int, sys.stdin.readline().split())
graph = []
for i in range(0, N):
    graph.append(list(map(int, sys.stdin.readline().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
population = 0

# 국경선을 열어줌
# VISITED[X] == 1 과 인접한 칸은 모두 국경선이 열림
def bfs(x, y, graph, visit):
    P = []  # 연합에 가입한 나라 좌표
    answer = 0

    Q = deque()
    Q.append((x, y))
    P.append((x, y))
    answer += graph[x][y]
    visit[x][y] = True

    while Q:
        x, y = Q.pop()

        for d in range(0, 4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    Q.append((nx, ny))
                    P.append((nx, ny))
                    answer += graph[nx][ny]
                    visit[nx][ny] = True
    population = answer // len(P)
    for x, y in P:
        graph[x][y] = population

    return True if len(P) >= 2 else False
day = 0
while True:
    visit = [[False] * N for _ in range(N)]
    stop = True

    for i in range(0, N):
        for j in range(0, N):
            if visit[i][j] == False:
                check = bfs(i, j, graph, visit)
                if check:
                    stop = False
    if stop:
        break
    else:
        day += 1

print(day)
