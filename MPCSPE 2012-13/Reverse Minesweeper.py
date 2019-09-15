#https://uchicago.kattis.com/problems/uchicago.mpcs.minesweeper
#Idea: extend the board outwards in four directions by 1, then we can update every original position using the same function 

x, y = map(int, input().split())
mine = []
for i in range(x):
    mine.append(list(map(int, input().split())))
sweep = [[0]*(y+2) for a in range(x+2)]  # extend the board outwards. Then the size of sweep is (x+2)*(y+2) 
def fill(i, j):     # the location (i,j) is a mine, fill(i,j) updated the 8 position that next to (i,j)
    l = [-1, 0, 1]
    for u in l:
        for v in l:
            if u == 0 and v == 0:
                continue            # skip the original point
            sweep[i+u][j+v] += 1    # the number of mines in this position added by 1

for i in range(x):
    for j in range(y):
        if mine[i][j] == 1:
            sweep[i+1][j+1] = 9  # the maximum possible number of a non-mine position is 8, hence we set mine to 9
            fill(i+1,j+1)        # Notice the location is shifted by 1 each direction

for s in range(1,x+1):
    for t in range(1,y+1):      # Only print the inner board of sweep
        if sweep[s][t] > 8:
            print('X', end='')
        elif sweep[s][t] == 0:
            print('-', end='')
        else:
            print(str(sweep[s][t]), end='')
        if t == y:
            print()
