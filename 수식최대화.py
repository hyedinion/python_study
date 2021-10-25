expression = "50*6-3*2"

def calculate(oper, numlist, operlist):
    rlist = []
    cnt = 0
    for i,o in enumerate(operlist):
        if o == oper:
            rlist.append(i)
            ln = numlist[i-cnt]
            rn = numlist[i+1-cnt]
            numlist.pop(i-cnt)
            if o=='-':
                numlist[i-cnt] = ln-rn
            elif o=='+':
                numlist[i-cnt] = ln+rn
            elif o=='*':
                numlist[i-cnt] = ln*rn
            cnt+=1
    
    cnt = 0
    for r in rlist:
        operlist.pop(r-cnt)
        cnt+=1
    return


import re
from itertools import permutations
def solution(expression):
    answer = 0
    #숫자추출
    numlist = list(map(int,re.findall('\d+',expression)))
    #숫자제거
    operlist = list(re.sub(r'[0-9]+', '', expression))

    oper = []

    for o in operlist:
        if o not in oper:
            oper.append(o)
    
    for nowOper in list(permutations(oper,len(oper))):
        nl = numlist[:]
        ol = operlist[:]
        for o in nowOper:
            calculate(o,nl,ol)
        answer = max(answer,abs(nl[0]))
        
    return answer

print(solution(expression))