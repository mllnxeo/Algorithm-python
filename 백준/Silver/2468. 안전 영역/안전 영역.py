from collections import deque

n = int(input())
array = []

for i in range(n):
    a = list(map(int, input().split()))
    array.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

max_safe_zone = 0
for h in range(0, 101):
    safe_zone = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n) :
            if array[i][j] > h and not visited[i][j] :
                bfs(i,j,h,visited)
                safe_zone += 1
    max_safe_zone = max(max_safe_zone, safe_zone)
print(max_safe_zone)