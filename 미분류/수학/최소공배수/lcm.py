def gcd(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

a,b = map(int,input().split())
lcm = a*b//gcd(a,b)
print(lcm)