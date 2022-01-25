#unionfind를 활용하여 최소신장트리를 구성한다.
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

import sys
#노드 개수와 간선(union 연산) 개수 입력 받기
v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v+1)

#간선정보
edges = []
result = 0
for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    #a, b노드가 이어진 간선의 비용은 c이다.
    edges.append((cost, a, b))
edges.sort() #오름차순 정렬

#크루스칼
for edge in edges:
    cost, a, b = edge
    #사이클 발생하지 않을때 union
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result = result + cost
    else:
        continue

print(result)