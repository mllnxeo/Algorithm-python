from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

# dfs
def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited1[i] :
            dfs(i)
# bfs
def bfs(start):
    queue = deque([start])
    visited2[start] = True

    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                queue.append(i)
dfs(v)
print()
bfs(v)