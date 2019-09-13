#https://uchicago.kattis.com/problems/uchicagoplacement.fill

def fill(a, i, v, x):
    if i < 0 or i >= len(a):
        return
    if a[i] != v:
        return
    if a[i] == x:
        return
    a[i] = x
    fill(a, i-1, v, x)
    fill(a, i+1, v, x)

N, I, X = map(int, input().split())
arr = list(map(int, input().split()))
V = arr[I]
fill(arr, I, V, X)
for j in range(N):
    print(arr[j], end=' ')
