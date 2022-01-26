#음수간선이 포함되어있는 상황에서의 최단거리
#벨만포드 알고리즘

#N개의 도시가 있다.
#한 도시에서 출발하여 다른 도시에 도착하는 버스가 M대가 있다.
#각 버스는 A, B, C로 나타내며 A는 시작도시, B는 도착도시, C는 소요시간이다.
#단, C가 양수가 아닌 경우가 있는데, C=0일때는 순간이동, C<0일때는 타임머신으로 되돌아가는 경우다.
#1번도시에서 출발하여 나머지 도시로 가는, 가장 빠른 시간을 구하는 알고리즘은?

##일단 음수간선인 경우가 있기 때문에 벨만포드 알고리즘.
##참고) 특정 도시에서 모든 도시로의 최단 경로이므로, 간선이 양수라면 다익스트라 사용
## 1<= N <= 500, 1<= M <=6000

import sys
INF = int(1e9)
#노드개수, 간선개수
n, m = map(int ,sys.stdin.readline().split())
#모든 간선에 대한 정보를 담는 리스트
edges = []
#최단 거리 테이블을 일단은 모두 무한으로 초기화
dist = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    #a에서 b로가는 비용이 c
    edges.append((a,b,c))

#벨만 포드 알고리즘
def bf(start):
    #최초 거쳐가는 노드는 자기자신, 거리는 0
    dist[start] = 0
    #모든 노드와 간선에 대해 반복
    for i in range(n):
        for j in range(m):
            #어차피 모든 간선을 확인해야하므로
            current_node = edges[j][0]
            next_node = edges[j][1]
            cost = [j][2]
            #현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[current_node] != INF and dist[next_node] > dist[current_node] + cost:
                dist[next_node] = dist[current_node] + cost
                # n번째 순환에서도 값이 갱신된다면 음수 순환이 존재하는 것으로 간주
                if i == n-1:
                    return True #음수순환이 존재
    return False

#알고리즘 수행
negative_cycle = bf(1) #출발노드는 1

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1): #1번노드를 제외하고, 다른 모든 노드로 가기위한 최단거리 출력
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i], end=' ')

