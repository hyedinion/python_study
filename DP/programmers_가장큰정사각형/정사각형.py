def find_square(I,J,depth,board):
    while True:
        flag = False
        depth+=1
        for newI in range(I,I+depth):
            flag = False
            newJ = J+depth-1
            if 0<=newI<len(board) and 0<=newJ<len(board[0])and board[newI][newJ] ==1:
                flag = True
            else:
                break
        if not flag:
            return (depth-1)**2

        for newJ in range(J,J+depth-1):
            flag = False
            newI = I+depth-1
            if 0<=newI<len(board) and 0<=newJ<len(board[0]) and board[newI][newJ] ==1:
                flag = True
            else:
                break
        if not flag:
            return (depth-1)**2

def solution(board):
    answer = 0
    I = len(board)
    J = len(board[0])
    
    for i in range(I):
        for j in range(J):
            if board[i][j]==1:
                answer = max(answer,find_square(i,j,1,board))

    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))

'''
[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	9
[[0,0,1,1],[1,1,1,1]]	4

1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

제한사항
표(board)는 2차원 배열로 주어집니다.
표(board)의 행(row)의 크기 : 1,000 이하의 자연수
표(board)의 열(column)의 크기 : 1,000 이하의 자연수
표(board)의 값은 1또는 0으로만 이루어져 있습니다.
'''