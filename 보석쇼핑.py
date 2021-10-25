gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

from itertools import product
def solution(gems):
    gemDict = {}
    for i,g in enumerate(gems):
        if g not in gemDict.keys():
            gemDict[g] = [i]
        else:
            gemDict[g].append(i)
            
    templist = [ [g] for g in gemDict[gems[0]]]
    
    #DIA에 대한 리스트를 만들껀데 dia 1부터 마지막까지 젤가까운 애들만 담기
    for j,g in enumerate(gemDict[gems[0]]):
        for k,v in gemDict.items():
            if k==gems[0]:
                continue
            else:
                minus = 99
                for i in v:
                    if abs(g-i)<minus:
                        templist[j].append(i)
                    



    answerlist = [1,1]
    absNum = 999
    for t in templist:
        mi = min(t)
        ma = max(t)
        a = abs(mi-ma)
        if absNum>a:
            answerlist[0] = mi+1
            answerlist[1] = ma+1
            absNum = a
        elif absNum==a:
            if answerlist[0]>mi:
                answerlist[0] = mi+1
                answerlist[1] = ma+1
                absNum = a

    return answerlist

print(solution(gems))