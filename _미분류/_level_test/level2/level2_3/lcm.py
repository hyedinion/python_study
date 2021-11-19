def gcd(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

def solution(arr):
    answer = 1
    for i,a in enumerate(arr):
        if i!=0:
            a//=gcd(arr[i],arr[i-1])
        answer*=a
    return answer

print(solution([12,18,2,24,3]))