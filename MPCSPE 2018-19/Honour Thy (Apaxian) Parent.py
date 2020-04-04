#https://uchicago.kattis.com/problems/apaxianparent

vowel = ['a', 'i', 'o', 'u']
Y, P = input().split()
ans = ""
if Y[-1] == 'e':
    ans = Y + 'x' + P
elif Y[-1] in vowel:
    ans = Y[:-1] + "ex" + P
elif Y[-2:] == "ex":
    ans = Y + P
else:
    ans = Y + "ex" + P
print(ans)
