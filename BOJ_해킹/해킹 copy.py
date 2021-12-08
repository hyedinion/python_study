import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N,D,C = map(int,input().split());C-=1
    parent = [[]for _ in range(N)]
    time = [9999 for _ in range(N)]
    for d in range(D):
        a,b,s = map(int,input().split());a-=1;b-=1
        parent[b].append([a,s])
    queue = deque()
    queue.append(C)
    time[C]=0
    while(len(queue)!=0):
        num = queue.popleft()
        for p in parent[num]:
            a,s = p
            time[a] = min(time[a],time[num]+s)
            queue.append(a)

    answer = 0
    answerCnt = 0
    for i in time:
        if i!=9999:
            answerCnt+=1
            answer = max(answer,i)
    print(answerCnt,answer)

