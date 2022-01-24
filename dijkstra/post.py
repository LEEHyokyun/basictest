#N개의 도시가 있고, 각 도시는 다른 도시로 우편을 보내고자 한다.
#단 X라는 도시에서 Y라는 도시로 전보를 보낸다고 할 때는 반드시 거쳐가는 통로가 존재해야 한다.
#어느날 C라는 도시에서 위급상황이 발생하여, 최대한 많은 도시로 최대한 빠르게 보내고자 한다.
#이때 도시C로부터의 우편을 받은 도시의 개수와, 메시지를 받기까지 걸린 총 소요시간은을 구하는 알고리즘은?

#첫째줄에 도시개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
#둘째줄부터 M+1번째 줄에 걸쳐 통로에 대한 정보 X, Y, Z(X에서 Y까지, 걸리는 시간Z)가 주어진다.
#첫째줄에 도시 C에서 받는 도시의 총 개수, 총 걸리는 시간이 공백으로 구분되어 출력된다.

##key point : 한 도시에서 다른 도시까지의 최단거리, 다익스트라.
##시간소요를 최소화하기 위해 우선순위 큐(min heap)을 사용.

import heapq
import sys
INF = int(1e9)
#노드 개수, 간선 개수, 시작 노드
n, m, start = map(int, sys.stdin.readline().split())
#편의성을 위해 index 1~n까지 구성되도록 설정
graph = [[] * (n+1) for _ in range(n+1)]
#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#간선 정보의 입력
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    #graph에 저장되는 정보는 x에서 y로 가는 비용이 z(최초비용)
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    #최초 시작노드에서 시작
    #거쳐가는 노드로 설정하여 거리를 0으로 최초 선언
    #heap에 저장되는 정보는 (최단거리, 끝 지점)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #heap에서 나온 것은 각 단계에서 노드까지 최단거리로 이미 정해짐
        dist, now = heapq.heappop(q)
        #dist 값이 초기화된 distance값보다 크면 반복진행하지 않음
        #이 의미는 visited 의미를 가지고 있음(방문노드 생략)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            #now가 거쳐가는 노드, i가 인접노드
            cost = dist + i[1] #i가 인접노드에 대한 정보, 첫번째 값이 비용
            if cost < distance[i[0]]: #cost: 거쳐가는 비용 / distance : 다이렉트
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#알고리즘 수행
dijkstra(start)

#결과값
count = 0
max_distance = 0
for d in distance:
    #도달할 수 있는 노드
    if d != INF:
        count = count + 1
        max_distance = max(d, max_distance)

#출력할때 시작노드는 제외
print(count-1, max_distance)

##
#3 2 1
#1 2 4
#1 3 2
