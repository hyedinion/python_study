import heapq
N,M = map(int,input().split())
edge = {}
indegree = {}
queue = []
for i in range(N):
    edge[i+1] = []
    indegree[i+1] = 0

for i in range(M):
    A,B = map(int,input().split())
    edge[A].append(B)
    indegree[B]+=1

for i in range(1,N+1):
    if indegree[i]==0:
        queue.append(i)
heapq.heapify(queue)

while queue:
    num = heapq.heappop(queue)
    print(num,end=" ")
    for e in edge[num]:
        indegree[e]-=1
        if indegree[e]==0:
            heapq.heappush(queue,e)

