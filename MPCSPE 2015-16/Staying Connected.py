#https://uchicago.kattis.com/problems/uchicagoplacement.connected

V = int(input())
E = int(input())
visited = [False] * V
G = [[] for v in range(V)]

def dfs(graph, root):
    visited[root] = True
    for vertex in graph[root]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(graph, vertex)

for i in range(E):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
ans = 0
for i in range(V):
    if not visited[i]:
        dfs(G, i)
        ans += 1
print(ans)
