import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int,input())))

Q = collections.deque([(0,0)])
result = 0

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                Q.append((nx, ny))
# print(graph)
print(graph[n - 1][m - 1])