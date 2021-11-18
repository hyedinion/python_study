N,K = map(int,input().split())
DP = [[0]*(N+1) for _ in range(K)]

for i in range(K):
    for j in range(N+1):
        if i==0:
            DP[i][j] = 1
        else:
            DP[i][j] = DP[i][j-1]+DP[i-1][j]

print(DP[N])
