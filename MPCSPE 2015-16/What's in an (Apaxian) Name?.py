#https://uchicago.kattis.com/problems/uchicagoplacement.apaxiannames

cnt = [0] * 4
com_name = input()
n = int(input())
for i in range(n):
    name = input()
    if name.find(com_name) == 0:
        cnt[0] += 1
    elif name.find(com_name) == -1:
        cnt[3] += 1
    elif name.find(com_name) == len(name) - len(com_name):
        cnt[1] += 1
    else:
        cnt[2] += 1
print(f"{cnt[0]} PRINCESS")
print(f"{cnt[1]} BARON")
print(f"{cnt[2]} PRIEST")
print(f"{cnt[3]} COMMONER")
