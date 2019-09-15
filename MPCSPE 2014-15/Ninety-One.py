#https://uchicago.kattis.com/problems/uchicago.mpcs.ninetyone

def m(n):
    if n > 100:
        return n - 10
    else:
        return m(m(n+11))

print(m(int(input())))
