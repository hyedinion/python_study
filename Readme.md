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
    <summary>시간복잡도</summary>
    <details>
        <summary>len()</summary>
        리스트의 len()함수가 O(1)인 이유
        Python에서 전체 요소의 개수를 리턴하는 len() 함수는 O(1)의 시간 복잡도를 가진다.
        어떻게 O(1)의 시간 복잡도를 가질 수 있었을까?
        len()은 __len__()을 호출한다.
        __len__()은 특별 메소드로 카운터로 작동하며 데이터가 정의되고 저장되면 자동적으로 증가한다.
        결과적으로 인터프리터에게 순회하며 길이를 가져오라는 명령대신 이미 저장된 value를 가져오게 된다.
        이렇게 len()은 O(1)의 시간 복잡도를 가지게 되었다
    </details>
</details>

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

    ## 그래프 만들기
    ```python
    graph = {}
    root = -1
    for i,pnode in enumerate(graph_list):
        if pnode==-1:
            root = i
            continue
        if pnode in graph.keys():
            graph[pnode].append(i)
        else:
            graph[pnode] = [i]
    ```
    > 1. 부모 노드가 주어졌을 때 graph[pnode]가 이미 존재하면 append해주고 없으면 graph[pnode]=[i]로 설정해준다.
    > 2. root 노드가 0번노드가 아닐 수 도 있기 때문에 조심!
    > - 자식 노드가 주어졌을 때는 root를 찾고 간단히 자신의 key값에 자식들을 넣어주면 된다.
    </details>

- <details>
    <summary>트라이</summary>

    - 문자열에서의 검색을 빠르게 해주는 자료구조
    - 트리를 사용
    - depth i에 해당하는 node는 문자열의 i번째 문자 이다.
    - 시간복잡도는 O(len(문자열))이지만 공간복잡도는 늘어나게 된다.
    ![img](https://user-images.githubusercontent.com/48575872/142189934-38396598-f76e-468f-8862-21b33c000013.png)
    </details>

</details>



<details>
    <summary>알고리즘</summary>

- <details>
    <summary>dfs</summary>
    
    - 깊이우선탐색
    - 조합이나 공간 탐색을 할 때 자주 씀
    - 보통 재귀함수로 구현한다.

    ```python
    def dfs(I,J,depth):
        if depth==maxDepth:
            answer+=1
            return
        if canGo(I,J):
            dfs(newI,newJ,depth+1)
        else:
            return
    ```
    - backtracking이란?
     - 탐색을하다 노드가 조건을 만족시키지 않으면 자식 노드들을 탐색하지 않고 바로 다음 노드로 넘어가는 것 (가지치기)
     - N-queens 문제가 대표적임
    </details>

- <details>
    <summary>bfs</summary>

    - 너비우선탐색
    - 탐색을 할 때 조건을 만족하는 최소 깊이를 구하여라 등 끝까지 탐색해볼 필요없이 최소 만족하는 깊이 까지만 탐색할 때 자주쓴다.
    - deque를 활용
    
    ```python
    from collections import deque
    queue = deque()
    queue.append(item)

    while queue:
        item = queue.popleft()
        if check(item):
            answer+=1
            for i in range(4):
                if canGo(newItem):
                    queue.append(newItem)
    ```
    - queue에 push와 pop을 많이 해야하므로 시간복잡도와 메모리를 생각해야한다.
    - 종료조건을 잘 설정해 주어야 시간초과가 나지 않는다.

    </details>

- <details>
    <summary>DP</summary>

    - 시간조건에따라 DP인지 완전탐색인지 구분하는게 중요
    - 점화식을 통해 이전에 풀었던 문제가 다음 문제를 푸는데 활용이 된다면 DP이다.
    - 이전에 구했던 정답들을 DP배열에 저장해두고 다음문제를 풀 때 이전의 정답들을 다시 구하지 않고 DP배열에서 꺼내쓴다.
    - DP방법을 생각하는게 어렵고 코드는 복잡하지 않다.
    - 대표적인 문제로 피보나치 수열이 있다.
    - i1 = 1 , i2 = 1 , i3 = 2 : i(n) = i(n-1)+ i(n-2)
    - i(n)을 구할 때 i(n-1)과 i(n-2)를 저장해두지 않았다면 다시 재귀함수를 통해 그 값들을 구해야 할 것이다. 시간복잡도 : O(n-1)+O(n-1)
    - 하지만 i(n-1)과 i(n-2)를 DP배열에 저장해 두었다면 DP[n-1]+DP[n-1] = DP[n] 이되어 시간복잡도가 O(1)이 된다.
    </details>

- <details>
    <summary>최소신장트리(MST)</summary>

    최소신장트리 (MST, Minimum Spanning Tree)
    1. Kruskal
    >- 그래프 내에 적은 숫자의 간선만을 가지는 ‘희소 그래프(Sparse Graph)’의 경우 Kruskal 알고리즘이 적합
    2. Prim
    >- 그래프에 간선이 많이 존재하는 ‘밀집 그래프(Dense Graph)’ 의 경우는 Prim 알고리즘이 적합하다.

    https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html

    ## Kruskal
    1. edge를 가중치 순으로 정렬한다.
    2. 작은 weight순으로 union_find()을 하여 union가능하면 weight++ 한다.

    ## Union_find()
    ### make_set(V)
    ```python
    for i in range(V):
        parent[i+1]=i+1
        rank[i+1]=0
    ```
    - 처음에 자기자신의 부모집합은 자신이기때문에 parent[]를 자기 자신으로 초기화 한다.
    - rank는 모두 0으로 초기화 한다.

    ### find(x)
    ```python
    if parent[x]==x:
        return x
    else:
        return find(parent[x])
    ```
    - find함수는 부모집합이 누구인지 알려준다.(즉, 부모집합이란 집합내에서 rank가 가장높은 node이다.)

    ### union(x,y)
    - 만약 그냥 parent[x] = y 라고 하면 find(x)함수로 부모를 찾는데 최악의 경우 O(N)만큼 걸린다.
    >- 최악의 경우 == 비대칭 트리, 연결리스트 상태

    - 해결법
    >1. Union by Rank
    >- 각 집합의 ‘rank’를, 더 큰 집합일수록 더 큰 rank를 가지도록 매긴다. 그리고 union 연산에서 언제나 더 작은 집합을 더 큰 집합에 합친다.
    >2. Path Compression
    >- Find(x)는 x에서 트리의 루트까지의 정점들을 차례대로 방문하는 형태로 구현한다. 경로 상의 모든 정점들을 모두 루트 정점을 바로 가리키게 한다.

    ### Union by Rank(x,y)
    ```python
    x = find(x)
    y = find(y)
    ```
    - 부모집합을 찾아 부모집합으로 비교를한다.
    ```python
    if x==y:
        return False
    ```
    - 같은 집합이면 union할 수 없음을 반환

    ```python
    if rank[x]>rank[y] : #x,y순서는 상관없음
        parent[y]=x
    else:
        parent[x]=y
        if rank[x]==rank[y]:
            rank[x]+=1
    return True
    ```
    - rank가 높은곳에 낮은 node를 union한다.
    - 만약 rank가 같다면 한쪽에 더해주고 더해준 쪽 rank를 +1해준다.
    - rank가 낮은곳에 union하게 되면 최악의 경우 tree가 한쪽으로 치우쳐 list의 형태처럼 된다. 이때 탐색을 진행하면 시간복잡도가 O(N)까지 증가해 효율성이 낮아진다.
    </details>

- <details>
    <summary>위상정렬</summary>
     
     - 만약 문제 조건에 먼저 풀어야 된다던가 먼저 지어야 되는 건물이 있다던가 "먼저"라는 단어가 나오고 순서를 지켜야 한다면 대부분 위상정렬 문제이다.
     - indegree활용 (부모의 갯수)

    ## 위상정렬
    - 위상정렬은 시작점이 존재해야하며, 사이클이 없는 유방향 그래프에서 탐색을 할 때 사용
    - 위상정렬은 답이 여러개가 될 수 있다.

    0. 간선을 탐색하며 자기 자신에게 연결된 간선 수 만큼 indegree+를 해준다.(먼저 수행되야하는 node의 갯수)
    1. indegree가 0인 node를 queue에 저장한다.(heapq사용, 문제에서 먼저 풀 수 있는건 먼저 풀어야 한다는 조건이 있기 때문)
    2. queue에서 차례로 node를 꺼내면서 그 node에 연결된 간선을 제거한다.(연결된 node의 indegree--)
    3. 만약 새롭게 indegree가 0이된 node가 있으면 queue에 넣는다.
    4. queue가 빌 때까지 2,3번을 반복한다.
    - 결과 : queue에서 꺼낸 순서

    </details>

- <details>
    <summary>이분탐색</summary>

    - 정렬되어 있는 list에서 특정 값이 어디에 있는지 빨리 찾고 싶을 때 이분탐색을 활용
    - start, end, mid를 활용

    1. start< end 일 때 까지 반복
    2. 만약 plist에 있는 숫자중 n보다 작거나 같은 수 중 가장 큰 값을 찾고 싶다면
    3. start = 0, end = len(plist), mid = (start+end)//2
    4. plist[mid]>n -> find(f,mid-1,n,plist)
    5. plist[mid]<=n -> find(mid+1,e,n,plist)

    ```python
    def find(f,e,n,plist):
    mid = (f+e)//2
    if f>e:
        return plist[e]
    if plist[mid]>n:
        return find(f,mid-1,n,plist)
    else:
        return find(mid+1,e,n,plist)
    ```

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
    - 시간복잡도
     - heapify O(N) -> 정렬후 pop해서 참조할 경우 유리,index로 참조불가능
     - list.sort() O(NlogN) -> 정렬후 index로 참조가능
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
    - 생성시 시간복잡도 O(n)
    ```python
    from collections import Counter
    Counter("hello")
    #{'h':1,'e':1,'l':2,'o':1}
    ```
    </details>
</detail>