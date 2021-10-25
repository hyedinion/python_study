T = int(input())
move = [(1,1),(1,-1),(-1,-1),(-1,1)]

def move_p( space, i, j, m, N, C, R, answerDict):
    global move
    pi = i
    pj = j
    answer = -1

    
    #move가 1,2일 때
    if m==1:    
    #전진 dfs
        #움직이기
        pi+=move[m][0]
        pj+=move[m][1]

        #벽을만날경우 다시돌아온 뒤 방향전환
        if pi>N-1 or pj>N-1 or pi<0 or pj<0:
            pi-=m[0]
            pj-=m[1]
            

        #같은 값을 방문했을 경우 종료
        key = space[pi][pj]
        if key in answerDict.keys():
            return -1
        
        #방문가능할 경우 저장
        answerDict[key] = 1

    #방향전환 dfs

    else:
        
    #move가 3,4일 때 계산후 return
        #C만큼이동
        #R만큼이동
        #가능시 return
        return




    answer = len(answerDict.items())
    if answer>1:
        return answer
    else:
        return -1

for t in range(T):
    N = int(input())
    space = [list(map(int,input().split())) for _ in range(N)]
    answer = -1
    
    for i in range(N-2):
        for j in range(1,N):
            answerDict = {}
            answer = max( answer, move_p(space,i,j,N,0,99,99,answerDict) )

    print('#{} {}'.format(t+1,answer))