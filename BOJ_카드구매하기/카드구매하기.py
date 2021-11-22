N = int(input())
P = list(map(int,input().split()))
W = [ [P[i]/(i+1),i+1] for i in range(N)]
W.sort(reverse=True)
answer =0 

for I in range(N):
    weight,num = W[I]
    answer += P[num-1]*(N//num)
    N-=num*(N//num)
    if N==0:
        break

print(int(answer))
