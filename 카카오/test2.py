place = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
#place = [["OOOOO", "OXXOX", "OOXOX", "OOXOX", "OOXXO"]]

def checkSafe(Place):
    move = [[ (0,1),(0,2),(1,1),(-1,1) ],[ (1,0),(2,0),(1,1),(1,-1) ],[ (-1,0),(-2,0),(-1,-1),(-1,1)],[(0,-1),(0,-2),(-1,-1),(1,-1)]]
    for i in range(5):
        for j in range(5):
            if Place[i][j]=='P':
                for M in move:
                    for k,m in enumerate(M):
                        if i+m[0]<0 or j+m[1]<0 or i+m[0] > 4 or j+m[1]>4:
                            break
                        if k==0:
                            if Place[i+m[0]][j+m[1]]=='X':
                                break
                        if Place[i+m[0]][j+m[1]]=='P':
                            return 0
    return 1


def solution(places):
    answer = []
    for P in places:
        answer.append(checkSafe(P))
    return answer

print(solution(place))