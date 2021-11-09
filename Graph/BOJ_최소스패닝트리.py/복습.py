V,E = map(int,input().split())
edge = []
for i in range(E):
    A,B,C = map(int,input().split())
    edge.append([C,A,B])
edge.sort()

parent = {}
rank = {}
for i in range(V):
    parent[i+1] = i+1
    rank[i+1] = 0

def union(a,b):
    x = find(a)
    y = find(b)
    if x==y:
        return False
    if rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        if rank[x]==rank[y]:
            rank[y]+=1
    return True

def find(i):
    if parent[i]==i:
        return i
    else:
        return find(parent[i])

def kruskal(edge):
    weight_sum = 0
    for e in edge:
        w,a,b = e
        if union(a,b):
            weight_sum+=w
    print(weight_sum)
    return

kruskal(edge)