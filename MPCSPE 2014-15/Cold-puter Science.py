#https://uchicago.kattis.com/problems/cold

n = int(input())
tps = list(map(int, input().split()))
cold = sum(tp < 0 for tp in tps)
print(cold)
