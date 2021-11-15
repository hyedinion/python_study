# python 알고리즘 문제풀이 정리

화이팅!

# Python 정리

### heapq
```python
    heapq.heapify(lst)
    heapq.heappush(lst, value)
    heapq.heappop(lst)
```

### deque
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

### string에서 숫자 추출
```python
import re

string = 'aaa1234, ^&*2233pp'
numbers = re.sub(r'[^0-9]', '', string)
print(numbers)
```

출처 : https://codechacha.com/ko/python-extract-integers-from-string/

### list

### dictionary
