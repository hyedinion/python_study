import sys
from collections import deque
input = sys.stdin.readline

def check_answer(time):
    answer = 0
    answerCnt = 0
    for i in time:
        if i!=9999:
            answerCnt+=1
            answer = max(answer,i)
    print(answerCnt,answer)
    return

def dijkstra(edge,time,C):
    queue = deque()
    queue.append(C)
    time[C]=0

    while(len(queue)!=0):
        cur = queue.popleft()
        for a,s in edge[cur]:
            temp = time[cur]+s
            if temp<time[a]:
                time[a] = temp
                queue.append(a)
    return

T = int(input())
for t in range(T):
    N,D,C = map(int,input().split());C-=1
    edge = [[]for _ in range(N)]
    time = [9999 for _ in range(N)]
    for d in range(D):
        a,b,s = map(int,input().split());a-=1;b-=1
        edge[b].append([a,s])

    dijkstra(edge,time,C)
    check_answer(time)