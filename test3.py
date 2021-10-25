ads = [[1, 3], [3, 2], [5, 4]]
#[[1, 3], [3, 2], [5, 4]] 20
#[[0, 3], [5, 4]] 0
#[[0, 1], [0, 2], [6, 3], [8, 4]] 40
#[[5, 2], [2, 2], [6, 3], [9, 2]] 33

def solution(ads):
    answer = 0
    answerDict = {}
    Tmin = 999
    for a in ads:
        key = a[0]
        value = a[1]
        if Tmin>key:
            Tmin = key
        if key not in answerDict.keys():
            answerDict[key] = [value]
        else:
            answerDict[key].append(value)

    available = []
    T = 0
    checkTime = 0
    while True:
        if T in answerDict.keys():
            for a in answerDict[T]:
                available.append(a)

        #재생하고 있는게 없을 때
        if checkTime ==0:
            if len(available)!=0:
                # 가능한 수 중 제일 비용이 큰것을 실행시킴
                available.remove(max(available))
                checkTime = 5

        for a in available:
            answer+=a

        if checkTime!=0:
            checkTime-=1

        T+=1
        if T>Tmin+5*(len(ads)-1)+1:
            break
    return answer

print(solution(ads))