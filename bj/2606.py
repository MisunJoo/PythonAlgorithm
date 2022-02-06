import sys
from collections import Counter

pc = int(sys.stdin.readline())
network = int(sys.stdin.readline())
graph = [[] for _ in range(pc + 1)]
visited = [False] * (pc + 1)

for i in range(network):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            visited[i] = True
            dfs(graph, i, visited)

dfs(graph, 1, visited)
counter =Counter(visited)
print(counter[True] - 1)