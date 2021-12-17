import heapq
N,D = map(int,input().split())
edge = {}
for i in range(N):
    start,end,distance = map(int,input().split())
    if start not in edge.keys():
        edge[start] = [[distance,end]]
    else:
        edge[start].append([distance,end])

distance = {}
queue = []
answer = D
heapq.heappush(queue,[0,0])
distance[0]=0

while queue:
    cur_distance,cur_node = heapq.heappop(queue)
    if cur_distance>distance[cur_node]:
        continue
    if cur_node in edge.keys():
        for next_distance,next_node in edge[cur_node]:
            new_distance = cur_distance+next_distance
            if next_node in distance.keys():
                if new_distance>=distance[next_node]:
                    continue
            distance[next_node] = new_distance
            if D-next_node+new_distance < answer:
                answer = D-next_node+new_distance
            heapq.heappush(queue,[new_distance,next_node])
print(answer)