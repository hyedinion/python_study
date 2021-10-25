n = 10
def solution(n):
    answer = 0
    bool_check = [True for _ in range(n+1)]
    for i in range(2,int(n**(1/2))+1):
        if bool_check[i]==True:
            p = i*i
            while p<=n:
                bool_check[p]=False
                p = p+i
    return bool_check.count(True)-2
print(solution(n))