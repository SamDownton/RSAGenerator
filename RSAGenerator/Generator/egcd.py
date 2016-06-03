'''
Created on 27 May 2016

@author: samuel.downton
'''
def egcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    else:
        return 0

def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True

# We define a function f(x,e,m) whose return value is x^e % m
def mod_exp(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y