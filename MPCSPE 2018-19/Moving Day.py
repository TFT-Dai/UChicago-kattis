#https://uchicago.kattis.com/problems/movingday

def product(l):
    ans = 1
    for x in l:
        ans *= x
    return ans

n, V = map(int, input().split())
v = []
for i in range(n):
    W = list(map(int, input().split()))
    v.append(int(product(W)))
print(max(v)-V)
