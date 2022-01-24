#거쳐가는 노드를 선택하는 과정에 heap을 활용하는 경우

import heapq
import sys

INF = int(1e9)

#노드개수, 간선개수
n, m = map(int, sys.stdin.readline().split())
#시작노드
start = int(input())
#그래프 연결 정보
graph = [[] for _ in range(n+1)]
#최단거리 테이블 초기화
distance = [INF] * (n+1)

#간선 정보
for _ in range(m):
    #a번 노드를 출발하여 b로 가는 비용이 c
    a, b, c = map(int, sys.stdin.readline().split())
    # 즉 graph에는 인접노드 정보와 함께 최초 상태의 비용까지 저장되어있게 된다.
    graph[a].append((b,c))

#개선 다익스트라
def dijkstra(start):
    q = []
    #heap에는 경로, 노드의 정보로 삽입하며
    #queue에 들어가는 정보는 거쳐가는 노드들에 대한 정보이다.
    #시작노드는 start에 저장된 상태
    heapq.heappush(q, (0, start))
    #최초거리정보 시작노드에 대해 0으로 초기화
    distance[start] = 0

    while q:
        #가장 최단 거리에 해당하는 노드를 꺼내고
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 방문한 노드라면 다음 반복문 실행
        if distance[now] < dist:
        #방문처리를 별도로 하지 않고, 현재 꺼낸 거리의 값이 더 크다면 이미 처리된 것(*그리디)
        #따라서 더이상 진행할 필요가 없음
            continue
        #현재 노드와 연결되어있는 인접노드들을 확인
        for i in graph[now]:
            cost = dist + i[1] #해당 노드를 거쳐 인접노드로 가는 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])



