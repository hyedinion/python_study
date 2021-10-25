def check_ready(work,done):
    znum = 0
    for n in range(work[2]):
        if work[n+3] in done:
            work[n+3] = -1
            znum+=1

    for z in range(znum):
        work.remove(-1)
    work[2]-=znum

    if work[2]==0:
        return True
    return False

#초기화
N = int(input())

time = 0
work = []
for n in range(N):
    work.append([n+1]+list(map(int,input().split())))

done = []
working = []
for w in work:
     if w[2]==0:
         working.append(w)
         work.remove(w)

while True:
    #종료조건
    if len(work)==0:
        max = 0
        for w in working:
            if w[1]>max:
                max = w[1]
        time+= max
        break
    #작업수행
    min = 9999
    for w in working:
        if w[1]<min:
            min = w[1]
    time +=min

    for w in working[:]:
        w[1]-=min
        if w[1]<=0:
            done.append(w[0])
            working.remove(w)
            
    #수행가능 체크
    for w in work[:]:
        if check_ready(w,done):
            working.append(w)
            work.remove(w)

    
print(time)