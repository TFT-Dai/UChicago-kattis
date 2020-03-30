#https://uchicago.kattis.com/problems/uchicago.mpcs.sinking

N, M, S, R = map(int, input().split())
H, P = 0, 0
ships = []
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
for i in range(S):
    ships.append(tuple(map(int, input().split())))
for i in range(R):
    hit = tuple(map(int, input().split()))
    if hit in ships:
        H += 1
        P += 1000
        ships.remove(hit)
    else:
        D = min(dist(hit, ship) for ship in ships)
        P += max(0, 1000 - D * 100)
print(f"{H}/{S} ships sunk. Score: {P} points")
