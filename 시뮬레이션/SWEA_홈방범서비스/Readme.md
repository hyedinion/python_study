# [SWEA]/[2117] 홈 방범 서비스 - python

## 분류
시뮬레이션

## 접근법
- 처음에 아무생각이 안났다.
- 이 큰 2차원배열을 다 탐색하면서 풀어야되는지 정말 의문이였는데 그게 정답이였다.
- 아무 아이디어가 생각나지 않아 친구들의 코드를 참조함

## 제약조건
- 서비스를 제공받는 집*지불하는돈 이 서비스를 제공하는 영역(비용)보다 크거나 같아야함
- 서비스는 한 공간에 하나만 제공가능

## 코드설명

```python
needMoney = size*size+(size-1)*(size-1)
```
- 마름모 (size = s)의 크기는 s*s+(size-1)*(size-1) 이다

### 내장함수
```python
def count_home(i,j,s,home):
    cnt = 0
    #집을 다 돌면서 마름모 영역안에 들어오는지 체크
    for h in home:
        if abs(i-h[0])+abs(j-h[1])<s:
            cnt+=1
    return cnt
```
- 마름모 size안에 들어온다는 말은 i,j의 이동이 size-1 보다 작다는 말이다.



## 후기
- 너무 큰 탐색범위가 나와서 어떻게 손대야 될지 몰랐다.
- 일단 고민되도 시작을 하면 답일 수 도 있다는 것을 알았다.
- 마름모가 나오면 항상 고민이 많이 되는것 같다.
- 마름모 공부를 더 해야겠다.

