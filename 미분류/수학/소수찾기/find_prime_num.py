def primeSieve(n):
    nlist = []
    prime = [True for _ in range(n+1)]
    for p in range(2,int(n**(1/2))+1):
        if prime[p]==True:
            i = p*p
            while i<=n:
                prime[i]=False
                i+=p
    for i,p in enumerate(prime):
        if i<2:
            continue
        if p:
            nlist.append(i)
    return nlist

def find(f,e,n,plist):
    mid = (f+e)//2
    if f>e:
        return plist[e]
    if plist[mid]>n:
        return find(f,mid-1,n,plist)
    else:
        return find(mid+1,e,n,plist)

N = int(input())
num_list = []
for n in range(N):
    num_list.append(int(input()))
maxN = max(num_list)
plist = primeSieve(maxN)

for n in num_list:
    print(find(0,len(plist)-1,n,plist))
