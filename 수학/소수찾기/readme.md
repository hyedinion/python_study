# 소수찾기

## 분류
에라토스테네스의 체

## 설명
- sqrt(n)+1 까지인 이유 <br>
> n==100 이라면 , sqrt(n) = 10<br>
> 소수가 아닌 합성수는 소수의 곱으로 이루어져 있으므로<br>
> 100이하의 수는 10보다 작거나같은 소수와 어떤소수의 곱으로 나타낼 수 있다.<br>
> 만약 11을 검사해본다면 <br>
> 11 * 7 은 i==7일 때 지워졌음<br>
> 11 * 11부터 확인해 보면 되는데 11*11보다 100이 작으므로 11은 확인해 볼 필요가 없다<br>
> python range()함수이기 때문에 1을 더해준다.<Br>


- i = p * p로 시작하는 이유<br>
>만약 p==7이라면<br>
>7+7 = 7 * 2 이미 앞에서 2의 배수는 제거해 주었음<br>
>... 7 * 6 이미 앞에서 3,2의 배수를 제거해 주었음<br>
>그래서 7 * 7부터 시작하면 된다.<br>

## main
- `nlist=[]` : 소수를 담을 배열
- `prime=[]` : prime[i]가 소수인지 check하는 boolean배열
- 2부터 sqrt(n)까지 돌면서 만약 p가 소수이면
- p*p부터 p를 더해가며 prime[i]에 False를 저장한다.

```python
def primeSieve(n):
    nlist = []
    prime = [True for _ in range(n+1)]
    for p in range(2,int(n**(1/2))+1):
        if prime[p]==True:
            i = p*p
            while i<=n:
                prime[i]=False
                i+=p
    for i in range(2,N+1):
        if prime[i]:
            nlist.append(i)
    return nlist
```