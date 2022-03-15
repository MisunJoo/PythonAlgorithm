import heapq
import sys

# 입력
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
start = 1
graph = [[]for i in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
  x, y = map(int, input().split())
  graph[x].append((y, 1))
  graph[y].append((x, 1))

# 다익스트라 구현
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while(q):
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

barn = 0
barn_distance = 0
same_distance = 0

for i in range(1, N+1):
  # print('barn', barn, 'distance[i]', distance[i])
  if barn <= distance[i]:
    barn = i
    barn_distance = distance[i]

same_distance = distance.count(barn_distance)
# print(distance)
print(barn, barn_distance, same_distance)

