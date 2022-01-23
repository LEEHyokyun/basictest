import sys
INF = int(1e9) #1*10^9

#노드 개수와 간선 개수
n, m = map(int, sys.stdin.readline().split())
#각 노드에 연결된 노드 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)] #노드 0은 제외
#방문정보
visited = [False] * (n+1)
#최단거리 테이블
distance = [INF] * (n+1)

#간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c)) #튜플 이용

#방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 반환
#거쳐가는 노드를 정하는 것
def get_smallest_node:
    min_value = INF
    index = 0 #최단거리가 짧은 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i] #현재 최단 거리, 방문하지 않은 노드를 거쳐가는 노드로 설정
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1): #시작노드를 제외한 나머지 노드에 대해 반복
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 노드
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[[j[0]]] = cost

#다익스트라 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리
for i in range(1, n+1):
    if distance[i] == INF:
        print("no path")
    else:
        print(distance[i])