# 4 Dijkstra Algorithm

graph = [
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0]
]

n = len(graph)
visited = [False] * n
dist = [9999] * n
dist[0] = 0

for i in range(n):
    min_val = 9999
    u = -1

    for j in range(n):
        if not visited[j] and dist[j] < min_val:
            min_val = dist[j]
            u = j

    visited[u] = True

    for v in range(n):
        if graph[u][v] > 0 and not visited[v]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

print("Shortest Distance =", dist)
