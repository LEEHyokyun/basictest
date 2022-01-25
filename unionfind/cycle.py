#기존 union find를 개선한 형태의 알고리즘
#특정 노드에 대한 루트노드 찾기
def findParent(parent, x):
    if parent[x] != x: #자기 자신이 아니라면, 해당 루트 노드의 루트노드를 찾는다.
        parent[x] = findParent(parent, parent[x]) #재귀호출이 아니라, TOpDown 방식으로 값을 저장한다.
    return parent[x]

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

#cycle판별 알고리즘 : cycle이 아닐 경우 union 과정 수행
cycle = False
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    if findParent(parent, a) == findParent(parent, b):
        cycle = True #루트노드가 같아서 cycle이 발생하였다면 즉시 반복문 종료
        break
    else:
        unionParent(parent, a, b)

if cycle:
    print("사이클이 존재하는 무향 그래프")
else:
    print("사이클이 존재하지 않은 무향 그래프")