#https://uchicago.kattis.com/problems/uchicago.mpcs.gcd

def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    if a < b:
        return gcd(a, b-a)

a, b = map(int, input().split())
print(gcd(a, b))
