# N * M 크기의 직사각형 형태 미로가 있다고 하자.
# 현재 위치는 1,1이고 미로의 출구는 N,M이다.
# 미로를 통과할 수 없는 부분을 0, 통과할 수 있는 부분을 1이라 할 때
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하는 알고리즘은?

# 간선의 비용이 모두 같은 상황에서 최단거리를 구하고 싶다면
# BFS

## 특정 노드를 방문하였을때 상하좌우가 모두 인접노드가 되고
## 이때 통과할 수 있는 노드를 Queue에 넣는다.

#기본 입력
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
     #상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue:
            #현재 좌표에서 이동할 수 있는 모든 경우의 수를 탐색
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                    continue #아래 구문을 무시하고 다음 반복을 실행
                if nx ==0 and ny == 0:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    #노드 수 누적
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

        #최종적으로 탈출 좌표에는 거쳐간 노드의 최소 개수가 기재되어있는 상태
        return graph[n-1][m-1]

print(bfs(0,0))