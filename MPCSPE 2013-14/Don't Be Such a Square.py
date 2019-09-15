#https://uchicago.kattis.com/problems/uchicago.mpcs.square

def exp(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n > 1 and (n % 2 == 0):
        return exp(x*x, int(n/2))
    if n > 1 and (n % 2 != 0):
        return exp(x*x, int((n-1)/2))*x

x, n = map(int, input().split())
print(exp(x, n))
