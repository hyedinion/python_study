def check_correct(P):
    if P=="":
        return True
    stack = []
    for p in P:
        if p=="(":
            stack.append(p)
        elif p==")":
            if len(stack)==0:
                return False
            else:
                stack.pop()
    return True

def u_v(P):
    lcnt = 0
    rcnt = 0
    for i,p in enumerate(P):
        if p=="(":
            lcnt+=1
        elif p==")":
            rcnt+=1
        if lcnt!=0 and rcnt!=0 and lcnt==rcnt:
            return [P[:i+1],P[i+1:]]
        
def change(P):
    stack = ""
    if P=="":
        return P
    for i in range(1,len(P)-1):
        if P[i]=="(":
            stack+=")"
        else:
            stack+="("
    return stack

def solution(p):
    if check_correct(p):
        return p
    u,v = u_v(p)
    if check_correct(u):
        return u+solution(v)
    else:
        return "("+solution(v)+")"+change(u)