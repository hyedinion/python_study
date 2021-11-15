def primeSieve(n):
    nlist = []
    prime = [True for _ in range(n+1)]
    for p in range(2,int(n**(1/2))+1):
        if prime[p]==True:
            i = p*p
            while i<=n:
                prime[i]=False
                i+=p
    for i in range(2,N+1):
        if prime[i]:
            nlist.append(i)
    return nlist

N = int(input())
print(primeSieve(N))