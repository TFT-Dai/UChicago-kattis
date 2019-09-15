#https://uchicago.kattis.com/problems/uchicago.mpcs.raindrops

n = int(input())
measure = list(map(int, input().split()))
cnt = sum(x >= 0 for x in measure)
tmp = sum(x for x in measure if x >= 0)
if cnt == 0:
    print("INSUFFICIENT DATA")
else:
    print(int(tmp / cnt))
