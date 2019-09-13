#https://uchicago.kattis.com/problems/uchicagoplacement.cgratio

N = int(input())
s = ''
for i in range(N):
    s += input()
ratio = (s.count('C') + s.count('G')) / len(s) * 100
print(ratio)
