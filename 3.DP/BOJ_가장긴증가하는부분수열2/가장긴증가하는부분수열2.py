import sys
input = sys.stdin.readline
N = int(input())
numList = list(map(int,input().split()))
answer = [numList[0]]

def find_index(i):
    start = 0
    end = len(answer)
    index = 0
    while start<=end:
        mid = (start+end)//2
        if answer[mid]>=i:
            end = mid-1
            index = mid
        else:
            start = mid+1
    return index

for i in range(1,N):
    if numList[i]>answer[-1]:
        answer.append(numList[i])
    else:
        index = find_index(numList[i])
        answer[index] = i

print(len(answer))


5