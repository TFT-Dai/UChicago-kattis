#https://uchicago.kattis.com/problems/uchicagoplacement.palindrome

def is_palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[-1]
    else:
        return is_palindrome(s[1:-1]) and (s[0] == s[-1])

word = input()
if is_palindrome(word):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
