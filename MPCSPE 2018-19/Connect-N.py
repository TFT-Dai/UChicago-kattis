#https://uchicago.kattis.com/problems/connectn

def check_win(x, y, n, board):
    b = "B" * n
    r = "R" * n

    # horizontal
    for i in range(x):
        s1 = "".join(board[i])
        if b in s1:
            return "BLUE WINS"
        if r in s1:
            return "RED WINS"

    # vertical
    for i in range(y):
        col = [r[i] for r in board]
        s2 = "".join(col)
        if b in s2:
            return "BLUE WINS"
        if r in s2:
            return "RED WINS"

    # principle diagonal
    for i in range(x - n, -1, -1):
        j = i
        k = 0
        diag = []
        while j < x and k < y:
            diag.append(board[j][k])
            j += 1
            k += 1
        s3 = "".join(diag)
        if b in s3:
            return "BLUE WINS"
        if r in s3:
            return "RED WINS"
    for i in range(1, y - n + 1):
        j = 0
        k = i
        diag = []
        while j < x and k < y:
            diag.append(board[j][k])
            j += 1
            k += 1
        s3 = "".join(diag)
        if b in s3:
            return "BLUE WINS"
        if r in s3:
            return "RED WINS"

    # counter diagonal
    for i in range(n - 1, y):
        j = 0
        k = i
        cdiag = []
        while j < x and k >= 0:
            cdiag.append(board[j][k])
            j += 1
            k -= 1
        s4 = "".join(cdiag)
        if b in s4:
            return "BLUE WINS"
        if r in s4:
            return "RED WINS"
    for i in range(1, x - n + 1):
        j = i
        k = y - 1
        cdiag = []
        while j < x and k >= 0:
            cdiag.append(board[j][k])
            j += 1
            k -= 1
        s4 = "".join(cdiag)
        if b in s4:
            return "BLUE WINS"
        if r in s4:
            return "RED WINS"

    return "NONE"


X, Y, N = list(map(int, input().split()))
Board = [['O'] * Y for i in range(X)]
for i in range(X):
    Board[i] = list(input().split())
print(check_win(X, Y, N, Board))
