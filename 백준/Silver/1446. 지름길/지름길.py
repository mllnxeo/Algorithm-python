import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n , d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))
    
for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d:  # D를 넘어가는 지름길은 무시
        continue
    graph[s].append((e, l))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  #dist : 비용

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
dijkstra(0)
print(distance[d])