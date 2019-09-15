#https://uchicago.kattis.com/problems/uchicago.mpcs.paxaai

def transform(s):
    if len(s) == 1:
        pass
    elif len(s) % 2 == 0:
        for i in range(int(len(s)/2)):
            s[2*i], s[2*i+1] = s[2*i+1], s[2*i]
    else:
        for i in range(int((len(s)-1)/2)):
            s[2*i], s[2*i+1] = s[2*i+1], s[2*i]
    return s

name = list(input())
result = "".join(transform(name))
print(result)
