#L, R, U, D
#여행가 A는 N*N크기의 정사각형 공간위에 서있다고 한다.
#이 공간의 최좌상단 좌표는 1,1이고 최우하단 좌표는 N,N이다.
#여행가 A가 상,하,좌,우 방향으로 이동할 수 있으며 시작좌표는 항상 1,1이다.
#여행가 A가 이동할 수 있는 이동명세서는 다음과 같다.
## L : 왼쪽 1칸, R : 오른쪽 1칸, U : 위쪽 1칸, D : 아래쪽 1칸
#이때 최종 좌표를 구하는 알고리즘은 무엇인가?
#단 정사각형 공간을 벗어나는 움직임은 pass한다.
import sys
#입력값
N = int(input())
plans = list(map(str, sys.stdin.readline().split()))
#현재위치
x, y = 1, 1
#L, R, U, D에 따른 명세서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']

#이동 계획에 따라 그대로 x+dx and y+dy
for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #nx, ny가 공간을 벗어나는 경우엔 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue #강제로 다음 반복을 수행
    x,y = nx, ny

print(x,y)