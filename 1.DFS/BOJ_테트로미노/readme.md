# [BOJ]/[14500] 테트로미노

## 분류
DFS

## 접근법
처음에는 우,하 방향으로만 가서 겹치는걸 방지하려고 했는데 못만드는 케이스가 많아서 안된다.<br>
그 다음에는 그냥 bruteforce로 다탐색했는데 ㅏㅓㅜㅗ 네개가 탐색이 안된다<br>
그냥 가능한 모양 다 저장하고 돌릴려고 하니까 한숨만 나와서 검색을 했다.<br>
- https://velog.io/@jajubal/파이썬백준-14500-테트로미노

## ㅏㅓㅜㅗ방향 탐색하는법
depth == 2 일 때 다음 블럭 탐색하는법<br>
1. 다음블럭이 갈수있는 곳이면 check배열에 체크, total에 더해준다
2. 하지만 시작 index만 다음 블럭이 아니라 다시 나의 블럭으로 설정 후 탐색을 한다.
- 마지막 블럭을 선택할 때 다시 나의 블럭을 시작으로 다음 블럭을 선택한다는게 중요한 생각인듯.
- 왜냐하면 depth에 영향을 주지않음 -> 하나만 더 선택하면 되기 때문
- 만약 depth==1일 때였다면 두개를 더 나의 블럭을 시작으로 골라야 하는데 (총 세블럭을 나를 시작으로 골라야 함) 첫번째 블럭은 선택됐고 두번째 블럭에 들어가면 depth가 증가하기 때문에 세번째 블럭을 선택할 수 없음. detph을 증가시키지 않으면 종료조건을 만족시키지 못함.

## 후기
음... 어렵당 ㅜ
- dfs에서 check배열을 쓸 때 나오면서 다시 원상태로 돌려주면 deepcopy를 쓰지 않아도 된다.! 다시한번 되새기자.
- 지금 코드에도 중복탐색한 블럭이 너무 많은데 줄이는 방법이 있는지 궁금하다.