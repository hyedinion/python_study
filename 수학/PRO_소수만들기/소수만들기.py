from itertools import combinations
def primeSeive(N):
    prime = [True for _ in range(N+1)]
    for p in range(2,int(N**(1/2))+1):
        if prime[p]:
            i = p*p
            while i<=N:
                prime[i]=False
                i +=p
    return prime

def solution(nums):
    answer = 0
    prime = primeSeive(3000)
    comb = list(combinations(nums,3))
    for c in comb:
        if prime[sum(c)]:
            answer+=1
    return answer

print(solution([1, 2, 3, 4]))