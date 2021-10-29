n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def solution(n, k, cmd):
    delList = []
    delDict = {}
    answer = []
    for i in range(n):
        answer+='O'
    for i in range(n):
        delDict[i] = 0


    for c in cmd:
        if len(c)>1:
            c,i = c.split()
            i = int(i)
        if c=='U':
            k -= i - (delDict[k] - delDict[k-i])
        elif c=='D':
            k += i - (delDict[k+i] - delDict[k])
        elif c=='C':
            delList.append(answer[:])
            answer[k] = 'X'
            for j in range(k):
                delDict[j]+=1
            if (k+delDict[k])==(n-1):
                k-=1
                k-=1
            else:
                k+=1
        elif c=='Z':
            answer = delList.pop()
        

    return ''.join(answer)

print(solution(n,k,cmd))