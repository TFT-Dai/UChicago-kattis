#https://uchicago.kattis.com/problems/uchicagoplacement.kmers

L, N, k, Q = input().split()
s = ''
for i in range(int(L)):
    s += input()
d = {}
for i in range(len(s) - int(k) + 1):
    substr = s[i:i+int(k)]
    if substr in d:
        d[substr] += 1
    else:
        d[substr] = 1
for i in range(int(Q)):
    q = input()
    if q in d:
        print(q, ' ', d[q])
    else:
        print(q, ' ', 0)
