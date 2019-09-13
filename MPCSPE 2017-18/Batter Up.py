#https://uchicago.kattis.com/problems/uchicagoplacement.batterup

n = int(input())
a = list(map(int, input().split(' ')))
sigma, count = 0, 0
for item in a:
    if item >= 0:
        sigma += item
        count += 1
print(sigma/count)
