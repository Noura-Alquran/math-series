

def fibonacci (n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(m):
    if m==0:
        return 2
    elif m == 1:
        return 1
    else:
        return lucas(m-1) + lucas(m-2)

def sum_series(x, a=0, b=1):
    if x == 0:
        return a 
    elif x == 1:
        return b 
    else:
        return sum_series(x - 1, a, b) + sum_series(x- 2, a, b)