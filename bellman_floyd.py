# 6(a) Bellman Ford

edges = [[0,1,6],[0,2,7],[1,2,8],[1,3,5],[1,4,-4],[2,3,-3],[2,4,9],[3,1,-2],[4,3,7]]
n = 5
dist = [9999] * n
dist[0] = 0

for i in range(n - 1):
    for e in edges:
        u,v,w = e
        if dist[u] != 9999 and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

print("Shortest Distance =", dist)

# 6(b) Floyd Warshall

INF = 9999

graph = [
[0,5,INF,10],
[INF,0,3,INF],
[INF,INF,0,1],
[INF,INF,INF,0]
]

n = len(graph)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for row in graph:
    print(row)
