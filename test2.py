array = [3, 5, 4, 1, 2]

#[3, 5, 4, 1, 2] [1, -1, 1, 2, 2]
#[1, 2, 3, 4, 5] [1, 2, 3, 4, -1]
#[7, 4, 4, 2, 9, 6] [4, 0, 0, 2, -1, 4]

def solution(array):
    stack = []
    answer = [-1 for _ in range(len(array))]
    stack.append(0)
    i = 1
    while stack and i<len(array):
        while stack and array[stack[-1]] < array[i]:
            answer[stack[-1]] = i
            stack.pop()
        stack.append(i)
        i+=1

    stack = []
    N = len(array)-1
    stack.append(N)
    i = N-1
    while stack and i>=0:
        while stack and array[stack[-1]] < array[i]:
            if answer[stack[-1]]>i:
                answer[stack[-1]] = i
            if answer[stack[-1]] ==-1:
                answer[stack[-1]] = i
            stack.pop()
        stack.append(i)
        i-=1
    return answer


print(solution(array))