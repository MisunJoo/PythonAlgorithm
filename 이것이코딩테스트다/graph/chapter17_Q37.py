import sys
N = int(sys.stdin.readline())  # 도시의 수
M = int(sys.stdin.readline())  # 버스의 수

dist = [[100001] * (N + 1) for _ in range(N + 1)]

# 입력받기
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a][b] = min(c, dist[a][b])

# 플로이드 와샬 알고리즘
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                dist[a][b] = 0
            else:
             dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if dist[a][b] == 100001:
            print("0",  end=" ")
        else:
            print(dist[a][b], end=" ")
    print()