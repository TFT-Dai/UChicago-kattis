#https://uchicago.kattis.com/problems/hailstone

def h(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n, *(h(int(n/2)))]
    else:
        return [n, *(h(int(3*n+1)))]
print(int(sum(h(int(input())))))
