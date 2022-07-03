origin = ["00110", "00011", "11111", "00000"]

graph = []
for i in range(len(origin)):
    line = []
    for j in range(len(origin[0])):
        line.append(int(origin[i][j]))
    graph.append(line)

N = len(graph)
M = len(graph[0])


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, 0)
        dfs(x + 1, 0)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
