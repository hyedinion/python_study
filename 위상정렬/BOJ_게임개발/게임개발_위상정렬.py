import heapq
N = int(input())
edge = {}
indegree={}
time = {}
queue = []
for i in range(N):
    time[i+1]=0
    edge[i+1] = []
    indegree[i+1] = 0

for i in range(1,N+1):
    ip = list(map(int,input().split()))
    time[i] = ip[0]
    for p in ip[1:]:
        if p==-1:
            break
        edge[p].append(i)
        indegree[i]+=1

for i in range(1,N):
    if indegree[i]==0:
        queue.append([time[i],i])
heapq.heapify(queue)

while(queue):
    num = heapq.heappop(queue)
    for p in edge[num[1]]:
        indegree[p]-=1
        if indegree[p]==0:
            time[p]+=time[num[1]]
            heapq.heappush(queue,[time[p],p])

for i in range(1,N+1):
    print(time[i])


#먼저 수행되는거 부터 수행해야함.
#heapq에 넣을 때 time이 작은 순으로 정렬해야함.
#그래야 time[p]+=time[num[1]] 여기서 오류가 안남