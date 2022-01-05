import sys
import operator

N = int(sys.stdin.readline())
table = [list(sys.stdin.readline().split()) for _ in range(N)]
answer = sorted(table, key=lambda x: (-int(x[1]), x[2], -int(x[3]), x[0]))

for i in answer:
  sys.stdout.write(i[0] + "\n")
