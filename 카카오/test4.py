#n = 3
#start = 1	
#end = 3
#roads = [[1, 2, 2], [3, 2, 3]]
#traps = [2]

n = 4	
start = 1	
end = 4
roads = [[1, 2, 1], [3, 2, 1],[2, 4, 1]]
traps = [2, 3]


import sys
sys.setrecursionlimit(10**6)

def trap(checkDict,t,trapDict):
    global traps
    appendList = []
    #trapDict = 딴곳 -> trap
    #checkDict = trap -> 딴곳
    if t in trapDict.keys():
        for tr in trapDict[t]:
            #딴곳에 있는것들 제거
            checkDict[tr[0]].remove((t,tr[1]))
            #다른 trap이 있을경우 trapDict에 저장해 줘야댐
            if tr[0] in traps:
                if tr[0] not in trapDict.keys():
                    trapDict[tr[0]] = [(t,tr[1])]
                else:
                    trapDict[tr[0]].append((t,tr[1]))
            #나중에 checkDict에 저장해야되니까 appendList에 저장
            appendList.append(tr)
        #trapDict에서 제거
        del trapDict[t]

    if t in checkDict.keys():
        checkList = checkDict[t]
        for c in checkList:
            keys = c[0]
            #checkDict에 있는것들 딴곳에 붙혀줌 (trap -> 딴곳) 방향바꿈
            if keys not in checkDict.keys():
                checkDict[keys] = [(t,c[1])]
            else:
                checkDict[keys].append((t,c[1]))
            #다시 trapDict만들어줌
            if t not in trapDict.keys():
                trapDict[t] = [c]
            else:
                trapDict[keys].append(c)

    #checkDict에 있는것들 제거 (trap -> 딴곳)
        del checkDict[t]
    checkDict[t] = appendList

def dfs(n,checkDict, end, traps,value,trapDict,depth):
    answer = 9999
    if depth>3000:
        return answer
    if n == end:
        return value
    if n in traps:
        trap(checkDict,n,trapDict)
    for c in checkDict[n]:
        i,v = c
        answer = min(answer,dfs(i,checkDict,end,traps,value+v,trapDict,depth+1))
    return answer

def solution(n, start, end, roads, traps):
    checkDict = {}
    trapDict = {}
    for r in roads:
        if r[0] not in checkDict.keys():
            checkDict[r[0]] = [(r[1],r[2])]
        else:
            checkDict[r[0]].append((r[1],r[2]))
        if r[1] in traps:
            if r[1] not in trapDict.keys():
                trapDict[r[1]] = [(r[0],r[2])]
            else:
                trapDict[r[1]].append((r[0],r[2]))
            

    answer = dfs(start,checkDict,end,traps,0,trapDict,0)

    return answer


print(solution(n, start, end, roads, traps))