N, M = map(int, input().split())

# basic setting
VERTICES_NUM = N
EDGES_NUM = M

# +1 for using original index
graph = [[] for _ in range(VERTICES_NUM + 1)]
visited = [False for _ in range(VERTICES_NUM + 1)]

# initializing
start_points = []
end_points = []

for _ in range(M):
    x, y = map(int, input().split())
    start_points.append(x)
    end_points.append(y)

for start, end in zip(start_points, end_points):
    graph[start].append(end)
    graph[end].append(start)

# dfs function
cnt = 0
def dfs(vertex):
    global cnt 
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)
    return

# simulation

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)
