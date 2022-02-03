import sys

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동방향(시계방향)에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

###########

def spreadVirus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                spreadVirus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def makeWall(cnt):
    global result
    if cnt == 3:
        # 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스 퍼트리기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    spreadVirus(i, j) # 여기서 해당 울타리가 쳐졌을 때 바이러스를 전부 퍼트림
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                makeWall(cnt)
                # 벽 만든 후 초기화
                data[i][j] = 0
                cnt -= 1

makeWall(0)