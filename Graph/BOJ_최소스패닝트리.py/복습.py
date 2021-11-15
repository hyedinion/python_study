V,E = map(int,input().split())
edge=[]
parent={}
rank={}
for i in range(1,V+1):
    parent[i]=i
    rank[i]=0

for i in range(E):
    A,B,C = map(int,input().split())
    edge.append([C,A,B])
edge.sort()

def kruskal(edge):
    total_sum = 0
    for e in edge:
        c,a,b = e
        if union(a,b):
            total_sum+=c
    return total_sum

def union(a,b):
    x =  find(a)
    y =  find(b)
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

print(kruskal(edge))