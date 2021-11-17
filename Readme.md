# python 알고리즘 문제풀이 정리

화이팅!

# Python 정리
참고 : https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/answers/4-python.md

### 파이썬의 주요 특징은?
- **인터프리터 언어**
    - 파이썬은 인터프리터 언어이므로, 실행하기 전에 컴파일을 할 필요가 없다.
    - 인터프리터로 동작하는 **스크립트 언어**이므로 다른 컴파일 언어에 비해 다소 느리다.
    - 컴파일러가 코드를 기계어로 번역해서 실행가능 파일을 만드는 것에 비해, 인터프리터는 코드를 한줄 씩 실행시간마다 번역해서 실행하기 때문이다.
- **동적타이핑(Dynamic Typing)**
    - 파이썬은 실행시간에 자료형을 검사하므로, 선언할 때 변수 유형을 명시할 필요가 없다.
    - `typing`이란 프로그램 내에서 변수의 데이터 타입을 정하는 것을 말한다. 데이터 타입 지정은 정적 또는 동적 타이핑으로 분류되는데, 프로그램 컴파일 시에 변수의 타입을 체크하는 `C`, `C++`과 같은 언어는 정적 타입 언어, 프로그램 실행 시에 타입을 체크하는 `Python`은 동적 타입 언어이다.
- **객체 지향 프로그래밍(OOP)**
    - 클래스와 구성 및 상속을 함께 정의할 수 있따는 점에서 객체 지향 프로그래밍에 매우 적합.
- **일급객체(First-class citizen)**
    - 파이썬에서는 `함수`와 `클래스`는 일급 객체이다. 일급객체는 변수나 데이터 구조 안에 담을 수 있고, 매개변수로 전달이 가능하며, 리턴값으로 사용될 수 있다는 특징을 가지고 있다


<details>
    <summary>자료구조</summary>

- <details>
    <summary>dict</summary>

    ### dict 딕셔너리
    - key,value로 구성
    - dict() 나 {}로 만들 수 있다.
    - key 중복 불가, 순서 없음
    ```python
        tempDict = {1:0,2:1,3:0}
        for v in tempDict.values():#O(1)
            print(v)
        for k in tempDict.keys():#O(1)
            print(v)
        for k,v in tempDict.items():#O(1)
            print(k,v)
        for k in tempDict:
            print(k)# in 은 key를 기준으로 for문을 돈다. 순서는 보장할 수 없다.
        del tempDict[1]

    ```
    </details>

- <details>
    <summary>set</summary>

    ### set 집합
    - key 값만 존재
    - set()이나 {}로 만들 수 있다.
    - key 중복 불가, 순서없음
    ```python
        tempSet = {1,2,3}
    ```
    </details>

- <details>
    <summary>tuple</summary>

    ### tuple 튜플
    - tuple()이나 ()로 만들 수 있다.
    - 리스트와 비슷하지만 항목값을 변화할 수 없다. (프로그램이 실행되는 동안 값이 바뀌지 않길 원하는 경우 사용)
    - del 안됨 -> 항목값을 변화 시킬 수 없기 때문
    - 1개의 요소만을 가질 때는 요소 뒤에 콤마(1,)를 반드시 붙여야 한다
    - 중복가능, 순서있음
    ```python
        tempTuple = (1,2,3)
    ```
    </details>

- <details>
    <summary>graph</summary>
    </details>

- <details>
    <summary>트라이</summary>
    </details>

</details>



<details>
    <summary>알고리즘</summary>

- <details>
    <summary>dfs</summary>
    </details>

- <details>
    <summary>bfs</summary>
    </details>

- <details>
    <summary>DP</summary>
    </details>

- <details>
    <summary>최소신장트리(MST)</summary>
    </details>

- <details>
    <summary>위상정렬</summary>
    </details>

- <details>
    <summary>이분탐색</summary>
    </details>



</details>



<details>
    <summary>python 내장함수</summary>

- <details>
    <summary>heapq</summary>

    ### heapq
    - heappush할 때 오름차순으로 list를 구성한다.
    ```python
        import heapq
        heapq.heapify(lst)
        #list to heapq
        heapq.heappush(lst, value)
        heapq.heappop(lst)
    ```
    </details>

- <details>
    <summary>deque</summary>

    ### deque
    - 앞,뒤 모두 push 와 pop이 가능하다.
    ```python
    from collections import deque
    deq = deque()
    # Add element to the start
    deq.appendleft(10)
    # Add element to the end
    deq.append(0)
    # Pop element from the start
    deq.popleft()
    # Pop element from the end
    deq.pop()
    ```
    </details>

- <details>
    <summary>re (string에서 숫자 추출)</summary>

    ### string에서 숫자 추출
    ```python
    import re
    string = 'aaa1234, ^&*2233pp'
    numbers = re.sub(r'[^0-9]', '', string)
    #12342233
    ```
    </details>

- <details>
    <summary>itertools 순열,조합</summary>

    ## python 순열, 조합
    ```python
    items = ['1', '2', '3', '4', '5'] 
    from itertools import permutations 
    list(permutations(items, 2)) 
    # [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')] 
    from itertools import combinations 
    list(combinations(items, 2))
    # [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
    ```
    </details>

- <details>
    <summary>counter</summary>

    - dict형
    - 각 key값이 몇번 나왔는지 cnt를 value로 함
    ```python
    from collections import Counter
    Counter("hello")
    #{'h':1,'e':1,'l':2,'o':1}

    ```
    </details>
</detail>