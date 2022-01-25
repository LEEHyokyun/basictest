#특정 노드에 대한 루트노드 찾기
def findParent(parent, x):
    if parent[x] != x: #자기 자신이 아니라면, 해당 루트 노드의 루트노드를 찾는다.
        return findParent(parent, parent[x])
        #parent[x], 즉 해당 루트노드의 루트노드를 찾는다.
        #parent는 부모테이블
    return x

#union 연산
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b: #a의 루트노드가 최종적인 루트노드가 되도록 노드 b를 설정
        parent[b] = a
    else :
        parent[a] = b

#입력
#노드개수와 간선개수
import sys
v, e = map(int, sys.stdin.readline().split())
#부모테이블
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

#Union 연산 수행
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    unionParent(a, b) #a와 b를 합치는 과정

#각 원소의 소속집합(루트노드)
for i in range(1, v+1):
    print(findParent(parent, i), end=' ')
print()
#부모테이블 내용
##부모테이블과 각자 속한 루트노드는 다른 내용일 수 있다(실제 루트노드는 거쳐거쳐 확인하므로)
for i in range(1, v+1):
    print(parent[i], end=' ')