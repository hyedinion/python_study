T = int(input())
d = [(0.5, 0), (-0.5, 0), (0, -0.5), (0, 0.5)]
def move(i):
    dy, dx = d[i[2]]
    return [i[0]+dx, i[1]+dy, i[2], i[3]]
def dicts(i):
    x, y = i[0], i[1]
    try:
        dic[(x,y)].append(i)  # 키값 중복시 자동 덮어씀 방지
    except:
        dic[(x,y)] = [i]  # dic[키값] = 개체

for t in range(T):
    N = int(input())
    answer = 0
    atom = [list(map(int, input().split())) for _ in range(N)]

    for i in range(4000):
        if len(atom) < 2:
            break
        dic = {}
        atom = list(map(move, atom)) #  moving
        list(map(dicts, atom))
        atom = []  # 새로운 info 준비
        for i in dic:  # i는 키값
            if len(dic[i]) > 1:  # 같은 위치에 원자가 두 개 이상인 경우
                item = dic[i]
                for e in item:
                    answer += e[3]
            else:
                item = dic[i]
                x = item[0][0]
                y = item[0][1]
                if -1000<=x<=1000 and -1000<=y<=1000:
                    atom.append(item[0])  # info 에 남아있는 원자들로 검사 진행

    print("#{} {}".format(t+1, answer))