# [programmers]/[스킬 체크 테스트2] 가장 큰 정사각형

## 문제
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.<br>
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요.<br>
(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)<br>

제한사항
표(board)는 2차원 배열로 주어집니다.<br>
표(board)의 행(row)의 크기 : 1,000 이하의 자연수<br>
표(board)의 열(column)의 크기 : 1,000 이하의 자연수<br>
표(board)의 값은 1또는 0으로만 이루어져 있습니다.<br>

## 분류
DP

## DP
[0][1]<br>
[2][3]<br>
3번이 0이 아닐 경우이다.<br><br>
3번은 0,1,2번 중 가장 작은 수+1을 해준다.<br>
정사각형의 한변의 길이를 저장해 주는 것이다.<br>
- 예시
만약 0,1,2 번이 1이라면 3번은 1+1한변의 길이가 2가 된다.
만약 0,1,2 번이 1,2,7이라면 3번은 1+1 한변의 길이가 2가 된다.
만약 0,1,2 번이 2,5,2이라면 3번은 2+1 한변의 길이가 3이 된다.


## 시뮬레이션
모든 인덱스를 다 돌면서 1이면 그 점이 정사각형의 첫번째 사각형이라고 생각한다.<br>
depth를 늘려가며 탐색<br>
1. depth==2:
> ㅢ 모양으로 증가하면서 모두 1인지 확인
> true면 계속진행
> false면 depth-1**2

## 후기
DP는 생각해내기 어렵다..