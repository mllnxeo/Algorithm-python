from collections import deque

m, n = map(int, input().split())
array = []
for i in range(n) :
    a = list(map(int, input().split()))
    array.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 1 :
            queue.append((i,j))

while queue :
    x,y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if array[nx][ny] == 0 :
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))

result = 0 #결과
for i in array :
    for j in i :
        if j == 0:
            print(-1)
            exit()
        result = max(result, j)
print(result-1)