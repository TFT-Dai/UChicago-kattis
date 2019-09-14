#https://uchicago.kattis.com/problems/uchicago.reversal

def reverse_recursive(s):
    if len(s) == 1:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

print(reverse_recursive(input()))
