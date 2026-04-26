# 5 Prim Algorithm

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

n = len(graph)
selected = [False] * n
selected[0] = True

for k in range(n - 1):
    min_val = 9999

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] > 0:
                    if graph[i][j] < min_val:
                        min_val = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, "=", graph[x][y])
    selected[y] = True


# 5 Kruskal Algorithm

edges = [[0,1,2],[1,2,3],[1,4,5],[0,3,6],[2,4,7]]
parent = [0,1,2,3,4]

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

for e in edges:
    u,v,w = e
    a = find(u)
    b = find(v)

    if a != b:
        print(u,"-",v,"=",w)
        parent[a] = b
