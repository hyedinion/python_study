numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

def calmove(hand, n):
    move = 0
    if n==0:
        n = 11
    if hand==0:
        hand =11
    if hand>n:
        while ((hand-1)//3)!=((n-1)//3):
            hand-=3
            move +=1
    else:
        while ((hand-1)//3)!=((n-1)//3):
            hand+=3
            move+=1
            
    return move+abs(hand-n)
    

def solution(numbers, hand):
    lhand =10
    rhand =12
    answer = ''
    Llist =[1,4,7]
    Rlist =[3,6,9]
    
    for n in numbers:
        if n in Llist:
            answer+='L'
            lhand = n
        elif n in Rlist:
            answer+='R'
            rhand = n
        else:
            lm = calmove(lhand,n)
            rm = calmove(rhand,n)
            if lm<rm:
                answer+='L'
                lhand = n
            elif rm<lm:
                answer+='R'
                rhand = n
            else:
                if hand=='right':
                    answer+='R'
                    rhand = n
                else:
                    answer+='L'
                    lhand = n
            
    return answer

print(solution(numbers,hand))