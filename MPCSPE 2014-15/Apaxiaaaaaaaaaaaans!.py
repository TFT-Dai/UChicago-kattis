#https://uchicago.kattis.com/problems/apaxiaaans

name = input()
ans = []
i = 0
while i < len(name):
    j = i + 1
    while j < len(name) and name[j] == name[i]:
        j += 1
    ans.append(name[i])
    i = j
print("".join(ans))
