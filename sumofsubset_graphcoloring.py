# 8 Sum of Subset

arr = [5, 10, 12, 13, 15, 18]
target = 30

def subset(i, total):
    if total == target:
        print("Found")
        return
    if i >= len(arr) or total > target:
        return

    subset(i + 1, total + arr[i])
    subset(i + 1, total)

subset(0, 0)


# 8 Graph Coloring

graph = [
[0,1,1,1],
[1,0,1,0],
[1,1,0,1],
[1,0,1,0]
]

color = [0,0,0,0]
m = 3

def safe(v,c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve(v):
    if v == len(graph):
        print(color)
        return

    for c in range(1,m+1):
        if safe(v,c):
            color[v] = c
            solve(v+1)
            color[v] = 0

solve(0)
