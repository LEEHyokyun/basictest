import sys

INF = int(1e9)
#노드, 간선 개수
n, m = map(int, sys.stdin.readline().split())
#graph 초기화, 최초 상태는 모두 INF
#노드1부터 간주하기 위해 n+1씩 반복
graph = [[INF] * (n+1) for _ in range(n+1)] #만드는 크기 자체는 n+1행 * n+1열

#자기자신에서 자기자신으로 가는 비용은 0으로 초기화
#n행 m열의 개념이 아닌, 노드 개수 n개와 간선 개수 m개에 유의한다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

#각 간선개수만큼 순회하여 간선 정보를 입력
for _ in range(m):
    #a에서 b로가는 비용은 c
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

#플로이드 워셜 알고리즘 적용 - 3중 반복
for i in range(1, n+1): #노드 개수만큼(n개), 가장 기준이 되는 반복인자(거쳐가는 기준 노드)
    for j in range(1, n+1): #노드 개수만큼(n개)
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

#수행결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF #도달할 수 없는 경우
            print("INFINITY")
        else:
            print(graph[i][j], end=" ")
            #그래프를 출력하되 같은 행에 대해서는 줄바꿈이 일어나지 않도록(공백표시)
    print() #같은 행 반복 후 줄바꿈

