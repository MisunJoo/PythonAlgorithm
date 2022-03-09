import sys
INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
# 간선 정보 초기화
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

# 플로이드 와샬 알고리즘
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:
        result += 1
print(result)