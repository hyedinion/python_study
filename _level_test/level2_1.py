def solution(brown, yellow):
    answer = []
    mult = brown+yellow
    for i in range(3,mult):
        if mult%i==0:
            if 2*(mult//i)+2*(i-2) ==brown:
                answer.append(mult//i)
                answer.append(i)
        if len(answer)!=0:
            break
    return answer

print(solution(10,2))