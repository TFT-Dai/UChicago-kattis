#https://uchicago.kattis.com/problems/queens
#Property: if the given positions are a solution, then every queen must have different x, y, x + y, y - x compared with others 
#   respectively. Hence, the total element number of sets {x}, {y}, {x+y}, {y-x} supposed to be 4 * size.

N = int(input())
queen = []
for i in range(N):
    queen.append(list(map(int, input().split())))
check_list = list(map(set, zip(*[(x, y, y + x, y - x) for x, y in queen])))
s = sum(len(x) for x in check_list)
if s == 4 * N:
    print("CORRECT")
else:
    print("INCORRECT")
