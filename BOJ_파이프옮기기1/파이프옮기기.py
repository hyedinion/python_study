import sys
input = sys.stdin.readline
N = int(input())
house = [ list(map(int,input().split())) for _ in range(N)]
pipe = [[0,0,0,1],1]
move = { 1: [ [[0,1,0,1],1],[[0,1,1,1],3] ] , 2: [ [[1,0,1,0],2],[[1,0,1,1],3] ], 3:[ [[1,1,0,1],1],[[1,1,1,0],2],[[1,1,1,1],3] ]}
answer = 0

def canGo (x,y):
    if 0<=x<N and 0<=y<N:
            return True
    return False

def check_margin(x1,y1,x2,y2):
    if not canGo(x1,y1) or not canGo(x2,y2):
        return False
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if house[x][y]==1:
                return False
    return True

def dfs(pipe):
    global answer
    direction = pipe[1]
    for m in move[direction]:
        new1x,new1y,new2x,new2y = [ x+y for x,y in zip(pipe[0],m[0])]
        if check_margin(new1x,new1y,new2x,new2y):
            if (new1x==N-1 and new1y==N-1) or (new2x==N-1 and new2y==N-1):
                answer+=1
                return
            dfs([[new1x,new1y,new2x,new2y],m[1]])

dfs(pipe)
print(answer)