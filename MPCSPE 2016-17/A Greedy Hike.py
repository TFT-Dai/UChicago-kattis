#https://uchicago.kattis.com/problems/uchicago.greedyhike

elev = []
X, Y = map(int, input().split())
xs, ys = map(int, input().split())
for i in range(X):
    elev.append(list(map(int, input().split())))
xe, ye = xs, ys
E = 0
while ye < Y-1:
    now_elev = elev[xe][ye]
    if xe == 0:
        #if there is only one row(X=1), just move forward
        if X == 1 or abs(elev[xe][ye] - elev[xe][ye+1]) <= abs(elev[xe][ye] - elev[xe+1][ye+1]):
            xe += 0
        else:
            xe += 1
    elif xe == X-1:
        if abs(elev[xe][ye] - elev[xe][ye+1]) <= abs(elev[xe][ye] - elev[xe-1][ye+1]):
            xe += 0
        else:
            xe += -1
    else:
        if (abs(elev[xe][ye] - elev[xe+1][ye+1]) < abs(elev[xe][ye] - elev[xe][ye+1]) and
            abs(elev[xe][ye] - elev[xe+1][ye+1]) <= abs(elev[xe][ye] - elev[xe-1][ye+1])):
            xe += 1
        elif abs(elev[xe][ye] - elev[xe-1][ye+1]) < abs(elev[xe][ye] - elev[xe][ye+1]):
            xe += -1
        else:
            xe += 0
    ye += 1
    E += abs(elev[xe][ye] - now_elev)

print(f"{xe} {ye} {E}")
