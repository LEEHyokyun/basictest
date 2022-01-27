#LCA, 최소공통조상

#N개의 정점으로 이루어진 트리가 주어진다.
#트리의 각 정점은 1번부터 N번까지 번호가 매겨져있고, 루트노드는 1번이다.
#두 노드의 쌍 M개가 주어져있을때, 두 노드의 가장 가까운 공통 조상을 구하는 알고리즘은?

import sys
n = int(sys.stdin.readline())

#1번 노드부터 각각의 부모노드를 기록할 배열 정보
parent = [0] * (n+1)
#각 노드의 깊이
#각 노드의 깊이가 계산되었는지의 여부
depth = [0] * (n+1)
isDepth = [False] * (n+1)
#graph 정보
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    #graph 정보
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs를 통해 모든 노드에 대해 깊이를 구한다.
def dfs(x, depth):
    isDepth[x] = True
    depth[x] = depth
    for y in graph[x]: #x노드에 대한 인접노드
        if isDepth[y]: #깊이 구했다면 continue
            continue
        parent[y] = x #하향탐색하는 과정으로, 부모노드의 정보를 입력
        dfs(y, depth+1)

#LCA
def lca(a,b):
    #두 노드의 depth를 동일하게 맞춘다
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    #깊이를 같게 만든 후, lca를 본격적으로 찾는다.
    while a != b:
        #각 노드의 부모노드까지 거슬러 올라간다
        a = parent[a]
        b = parent[b]
        return a

#결과출력
dfs(1,0)

#반복횟수
m = sys.stdin.readline()
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a,b))
