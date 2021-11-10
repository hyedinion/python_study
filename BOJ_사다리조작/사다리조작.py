import sys
from collections import deque
input = sys.stdin.readline

N,M,H = map(int,input().split())
check = [ [True]*(N+1) for _ in range(H+1) ]
answer = -1
for i in range(M):
    A,B = map(int,input().split())
    check[A][B] = False
    check[A][B+1] = False

def check_answer(check):
    for i in range(1,N+1):
        currentI,currentJ = 1,i
        while currentI!=H:
            if not check[currentI][currentJ]:
                if not check[currentI][currentJ+1]:
                    currentJ+=1
                else:
                    currentJ-=1
            currentI+=1
        if currentJ!=i:
            return False
    return True

queue = deque()
queue.append([0,0,0,[]])
while(queue):
    I,J,depth,append_list = queue.popleft()
    if check_answer(check):
        answer = depth
        break
    if check[I][J] and check[I][J+1] and depth<3:
        check[I][J]=False
        check[I][J+1]=False
        
        check
print(answer)

