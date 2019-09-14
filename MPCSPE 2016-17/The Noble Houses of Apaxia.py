#https://uchicago.kattis.com/problems/uchicago.noble

first, last = input().split()
noble_name = first + ' ' + last * (len(last) if len(last) != 5 else 4)
print(noble_name)
