S = "2three45sixseven"

def solution(S):
    checkDict = { 
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five': '5',
    'six':'6',
    'seven': '7',
    'eight':'8',
    'nine':'9',
    }

    answer = ''
    checkS = ''
    for i,s in enumerate(S):
        if ord(s)>=ord('0') and ord(s)<=ord('9'):
            answer+=s
        else:
            checkS+=s
            if checkS in checkDict.keys():
                answer+=checkDict[checkS]
                checkS=''


    return int(answer)


print(solution(S))