#https://uchicago.kattis.com/problems/uchicagoplacement.grotesque

measure = list(map(int, input().split()))
if sum(measure) >= 30 or max(measure) == 6:
    print("CLEAN")
else:
    print("DO NOT CLEAN")
