T = int(input())

def move_p( space, i, j, move, N):
    pi = i
    pj = j
    answerDict = {}

    #4방향으로 탐색시작
    for m in move:
        #벽을 만날 때 까지 반복
        while(True):
            #움직이기
            pi+=m[0]
            pj+=m[1]

            #벽을만날경우 다시돌아온 뒤 방향전환
            if pi>N-1 or pj>N-1 or pi<0 or pj<0:
                pi-=m[0]
                pj-=m[1]
                break

            #같은 값을 방문했을 경우 종료
            key = space[pi][pj]
            if key in answerDict.keys():
                return -1
            
            #방문가능할 경우 저장
            answerDict[key] = 1

    answer = len(answerDict.items())
    if answer>1:
        return answer
    else:
        return -1

for t in range(T):
    N = int(input())
    space = [list(map(int,input().split())) for _ in range(N)]
    answer = -1
    move = [(1,1),(1,-1),(-1,-1),(-1,1)]
    for i in range(N-2):
        for j in range(1,N):
            answer = max( answer, move_p(space,i,j,move,N) )

    print('#{} {}'.format(t+1,answer))