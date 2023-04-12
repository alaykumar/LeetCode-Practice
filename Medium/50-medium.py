def mul(x, n):
    ans = 0
    while n > 0:
        ans += x*x
        n -= 1
        print(ans, n)
    #return float(ans)
    print(float(ans))

def mulNeg(x,n):
    ans = 0
    while n < 0:
        ans += x*x
        n += 1
    #return float(1/ans)
    print(float(1/ans))
    

x = 2
n = 10

if n == 0:
    print(float(1))
elif n > 0:
    mul(x,n)
elif n < 0:
    mulNeg(x,n)