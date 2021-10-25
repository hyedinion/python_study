def count_home(i,j,s,home):
    cnt = 0
    for h in home:
        if abs(i-h[0])+abs(j-h[1])<s:
            cnt+=1
    return cnt

T = int(input())

for t in range(T):
    N,M = map(int,input().split())
    space = []
    home = []
    answer = 0
    for n in range(N):
        space.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if space[i][j]==1:
                home.append((i,j))

    size = 1
    for i in range(N+1):
        needMoney = size*size+(size-1)*(size-1)
        for i in range(n):
            for j in range(n):
                h = count_home(i,j,size,home)
                if needMoney<=h*M:
                    if answer<h:
                        answer = h

        
        size+=1

    print("#",end='')
    print(t+1,end=' ')
    print(answer)
