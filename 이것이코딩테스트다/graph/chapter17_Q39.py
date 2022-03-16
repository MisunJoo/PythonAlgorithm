import heapq
import sys

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]
    while q:
        value = heapq.heappop(q) # 거리, 현재 x, 현재 y
        x = value[1]
        y = value[2]
        if distance[x][y] < value[0]:
            continue
        for i in range(4): # 생각 못한 부분. 상하좌우 인접한 곳으로 1칸씩 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            cost = value[0] + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))




T = int(sys.stdin.readline())
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(T):
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N)]
    for j in range(0, len(graph)):
        graph[j] = list(map(int, sys.stdin.readline().split()))
    distance = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    dijkstra(0, 0)
    print(distance[N - 1][N - 1])
