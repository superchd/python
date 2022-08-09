from collections import deque

def bfs(queue, node, edge, visited, n):
    connected = 0

    while queue:
        v = queue.popleft()
        # vertex에 연결된 edge의 개수 구하기
        #print(v, end = ' ')
        connected += 1
        k = edge[v]
        for i in range(1, k + 1):
            next = node[v][i]
            # 이미 네모칸을 방문했다면 무시
            if visited[next] == 1:
                continue
            # 방문안한 vertex들을 queue에 넣음
            queue.append(next)
            visited[next] = 1
    return (connected, n - connected)

def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        node = [[0] * 100 for _ in range(100)]
        edge = [0 for i in range(100)]
        visited = [0 for i in range(100)]

        # 그래프 그리기
        for w in wires:
            if wires[i] != w:
                edge[w[0]] += 1
                edge[w[1]] += 1
                node[w[0]][edge[w[0]]] = w[1]
                node[w[1]][edge[w[1]]] = w[0]

        result = 0
        # bfs를 통해 연결되어있는 덩어리의 개수를 구해보자
        for j in range(1, n):
            queue = deque()
            queue.append(j)
            if visited[j] == 0:
                visited[j] = 1
                c, u = bfs(queue, node, edge, visited, n)
                result += 1
                val = abs(c - u)
                print(f'val = {val}')
                answer.append(val)
    
    print(min(answer))

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n, wires)