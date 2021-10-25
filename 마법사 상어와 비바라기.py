import sys
input = sys.stdin.readline
d = [[],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

N,M = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(N)]
move = [list(map(int,input().split())) for _ in range(M)]
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
check_cloud = [[False]*N for _ in range(N)]
new_cloud = []

def in_range(N,r,c):
    if r>=N:
        return False
    elif c>=N:
        return False
    elif r<0:
        return False
    elif c<0:
        return False
    else:
        return True

for m in move:
    for cl in cloud:
        cl[0]+=d[m[0]][0]*m[1]
        cl[1]+=d[m[0]][1]*m[1]
        cl[0] = cl[0]%N
        cl[1] = cl[1]%N
        #1더하기
        space[cl[0]][cl[1]]+=1
        check_cloud[cl[0]][cl[1]]=True
    for cl in cloud:
        for i in range(2,9,2):
            r = cl[0]+d[i][0]
            c = cl[1]+d[i][1]
            if in_range(N,r,c):
                if space[r][c]!=0:
                    space[cl[0]][cl[1]]+=1
    
    for i in range(N):
        for j in range(N):
            if space[i][j]>=2:
                if not check_cloud[i][j]:
                    new_cloud.append([i,j])
                    space[i][j]-=2

    cloud = new_cloud
    new_cloud = []
    check_cloud = [[False]*N for _ in range(N)]

answer = list(sum(s) for s in space)
print(sum(answer))




