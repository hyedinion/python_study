inputString = "line [({<plus>})"
#Hello, world! 0
#line [({<plus>)}] -14
#line [({<plus>}) -15
#>_< 0
#x * (y + z) ^ 2 = ? 1

def solution(inputString):
    checkList = ['(','{','[','<']
    checkList2 = [')','}',']','>']
    resultNum  = 0
    inList = []
    for i,s in enumerate(inputString):
        for j,c in enumerate(checkList):
            if s==c:
                inList.append(checkList2[j])
        if s in checkList2:
            if len(inList)==0:
                return i
            if s!= inList.pop():
                return -1*i
            else:
                resultNum+=1

    if len(inList)!=0:
        return -1*(len(inputString)-1)
    else:
        return resultNum

print(solution(inputString))