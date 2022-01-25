from collections import deque
import sys

#노드 개수와 간선 개수
v, e = map(int, sys.stdin.readline().split())
#진입차수배열(노드는 1부터 시작)
indegree = [0] * (v+1)
#graph 간선정보
graph = [[] * (v+1) for _ in range(v+1)]

#방향그래프 간선정보(각 노드별 인접노드를 입력받는다)
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) #a > b 통로
    indegree[b] = indegree[b] + 1

#위상정렬 수행
def topologySort():
    result = []
    q = deque()
    # 최초 queue에 진입차수가 0인 노드를 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        #인접노드
        for i in graph[now]:
            indegree[i] = indegree[i] - 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i,end=' ')#결과출력

topologySort()