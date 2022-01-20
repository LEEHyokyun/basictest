#graph 형태로 모델링할 수 있다면 1차 의심
#노드의 인접노드를 파악해야 한다면 2차의심
#이동가능한 모든 인접노드를 파악하고 방문처리 해야한다면 확신

# N * M 크기의 얼음틀이 있다.
# 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 나타낸다.
# 구멍이 뚫려있는 부분끼리 상,하,좌,우 한 부분이라도 연결되어있다면 하나의 얼음으로 간주한다.
# 얼음 틀 모양이 주어졌을때, 생성되는 구멍뚫린 얼음의 총 개수를 구하는 알고리즘은?

# 첫째줄에 얼음 틀의 세로 길이(N행), 얼음 틀의 가로 길이(M열)가 입력된다.
# 둘쨰줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.

## 먼저 값이 0이면서 방문하지 않은 특정지점에서 부터 시작
## 특정 지점의 상, 하, 좌, 우를 살펴 인접 지점에서 방문하지 않은 지점이 있다면 방문
## 해당 방문 지점에서 인접노드를 살펴보고 방문, 이 과정을 반복
## 방문하지 않은 0의 지점 수를 카운트.

#기본 입력(공백기준)
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    #입력받은 값을 배열(리스트) 형태로 저장후 graph정보에 넣기
    graph.append(list(map(int, sys.stdin.readline().split())))

#dfs
#인접노드를 계속해서 파고들면서 파악하므로 dfs
def dfs(i, j):
    #먼저 범위 밖이면 dfs 종료
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if graph[i][j] == 0:
        # 방문하고
        graph[i][j] == 1
        #그 인접노드까지 모두 방문이 종료되어야, 모든 알고리즘을 종료
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    else: #graph 지점이 1인 경우엔 pass
        pass
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result = result + 1

