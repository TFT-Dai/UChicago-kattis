#https://uchicago.kattis.com/problems/uchicago.calendar

def calendar_format(a, b, c):
    if a > 31:
        return "Format #3"
    elif 31 >= a > 12:
        if c > 31:
            return "Format #2"
        else:
            return "Ambiguous"
    else:
        if b > 12:
            return "Format #1"
        else:
            return "Ambiguous"

a, b, c = map(int, input().split())
print(calendar_format(a, b, c))
