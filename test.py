def solution(numbers):
    answer = ''
    numbers.sort(reverse=True,key = lambda x: x*100+x*10+x if x<10 else (x*10+x//10 if x<100 else x))
    print(numbers)
    for i in numbers:
        answer+=str(i)
    return answer

print(45//10)
print(solution([ 67,676,677]))

#344 34
#34 344