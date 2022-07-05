N = 5
M = 6
original = ["101010", "111111", "000001", "111111", "111111"]
graph = []
for i in range(len(original)):
    line = []
    for j in range(len(original[0])):
        line.append(int(original[i][j]))
    graph.append(line)

N = len(graph)
M = len(graph[0])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[N - 1][M - 1]


print(bfs(0, 0))
