#1번부터 N번까지의 빌딩이 있고, 서로 도로를 통해 연결되어있다.
#A라는 사람이 1번 회사에 위치해 있고, X번 회사에 방문 후 물건을 판매하고자 한다.
#X번 회사에 방문 후 K번 회사에 방문하여 소개팅까지 진행한다.
#각 빌딩은 양방향 이동이 가능하고, 1만큼의 시간이 소요된다.

#1번회사에서 출발하여 K번 회사에 방문, X번 회사로 가고자 할 때
#회사 사이를 이동하면서 걸린 최소 소요시간을 구하는 알고리즘은?

#첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 제시된다.
#각 N, M은 1~100사이의 양의 정수이다.
#둘쨰 줄부터 M+1번째 까지 연결된 두 회사의 번호가 공백으로 주어진다.
#M+2번째 줄에는 X와 K 공백으로 주어진다.
#A가 K를 거쳐 x로 이동하는 최소 이동시간을 출력하고, 이동 불가 시 -1을 출력한다.

##노드의 선택 기준이 거쳐가는 노드로, 전형적인 플로이드 와샬 구현 유형
##노드가 최대 100이므로, 플로이드 워셜 알고리즘을 이용해도 효율적(*문제 자체가 최단거리)
##플로이드 워셜을 적용한다면 1번노드에서 k까지의 소요시간과 K에서 X까지의 소요시간을 더하면 된다.
import sys

INF = int(1e9)

#노드와 간선의 개수
n, m = map(int, sys.stdin.readline().split())
#2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신에서 자기자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    #각 행열값은 행에서 열로가는 시간(비용)을 의미
    #다익스트라와 마찬가지로, 2중반복이 아닌 간선 개수만큼 반복함에 유의
    graph[a][b] = 1
    graph[b][a] = 1

#거쳐갈 노드 K와 목적지 노드 X를 입력
k, x = map(int, sys.stdin.readline().split())

#플로이드 와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

#수행결과 출력
distance = graph[1][k] + graph[k][x]

if distance == INF:
    print(-1)
else:
    print(distance)