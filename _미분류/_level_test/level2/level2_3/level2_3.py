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

def solution(arr):
    prime = {}
    for p in primeSieve(100):
        prime[p]=0
    for num in arr:
        for p in prime.keys():
            if num<p:
                break
            count = 0
            while True:
                if num%p==0:
                    count+=1
                    num//=p
                else:
                    prime[p] = max(count,prime[p])
                    break               
    answer=1
    for k,v in prime.items():
        if v!=0:
            answer*=k**v
    return answer

print(solution([12,18,2,24,3]))