# # [SWEA]/[2112] 보호필름 - python 

## 분류
DFS

## 접근법
- 가지치기를 하면 겹치는 수정범위에서 시간을 단축할 수 있다는 생각이 먼저 들었다.
- 그래서 bfs로 하면 옆으로 커지는 탐색이니깐 약물 투여 횟수를 늘려가며 탐색하는 것과 같다고 생각하고 bfs로 탐색해야 겠다고 생각했다.
- 하지만 list에 append하고 pop하는 과정이 꽤나 시간이 오래걸리는 것 같았다.
- dfs로 수정하고 재귀함수로 풀었더니 통과가 됐다. (물론 조건을 걸어 backTracking 해줬다)


## DFS vs BFS

1. DFS
- 일단 space 등 변수들을 따로 저장할 필요가 없다.
- 코드를 재귀함수로 간단하게 짤 수 있다

2. BFS
- 계속 수정되는 값을 저장까지 해야하기 때문에 이때 시간이 많이 걸리는 것 같다.
- queue를 통해 인자들을 저장하고 불러와 줘야해서 메모리, 시간 측면에서 모두 별로인듯 하다

3. 참고
- 처음에는 DFS코드에서 backTracking 종료조건을
```python
if n>=K:
    return -1
```
K보다 약물투여 횟수가 크면 종료하게 했다
<br>

- 현재 코드는 아예 answer가 나오면 global answer에 저장하고 그 answer보다 작으면 종료하게 했다.
- 시간이 훨씬 단축됨
```python
if n>=answer:
    return answer
```

## 코드설명

space : 보호필름<br>
lineCheck : 어떤 row에 약물을 투여했는지 check, 투여했으면 1 아니면 0<br>
checkLine() : 보호필름(space)이 합격인지 확인<br>
change_space() : space를 수정후 재귀함수 호출 (dfs)<br>


## 후기
- 당연히 BFS를 사용하면 약물투여가 작은 순서대로 탐색하기 때문에 시간이 더 적게 걸릴줄 알았는데 아니였다.
- 거의 완전탐색하는 DFS가 시간이 더 적게 걸렸다. 심지어 재귀함수인데...
- 왜 그런지 잘 모르겠지만 list에 저장하고 빼는게 생각보다 시간이 오래걸리는 것 같다. 물론 변수 복사도...
- 앞으론 DFS만 쓸거다🥲