#https://uchicago.kattis.com/problems/uchicago.mpcs.tricky

N = int(input())
alpha = {"J": 11, "Q": 12, "K": 13, "A": 14}
def poker(card):
    if card in alpha:
        return alpha.get(card)
    else:
        return int(card)
P1 = [poker(x) for x in input().split()]
P2 = [poker(x) for x in input().split()]
score = [0, 0]
score[0] = sum(P1[i] > P2[i] for i in range(N))
score[1] = sum(P1[i] < P2[i] for i in range(N))
if score[0] > score[1]:
    print("PLAYER 1 WINS")
elif score[0] < score[1]:
    print("PLAYER 2 WINS")
else:
    print("TIE")
