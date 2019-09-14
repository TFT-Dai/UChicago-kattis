#https://uchicago.kattis.com/problems/uchicagoplacement.martingale

m1 = int(input())
b1 = int(input())
n = int(input())
outcome = list(map(int, input().split()))
rd = 0
bet = b1
while rd < n:
    if outcome[rd] == 1:
        m1 += bet
        bet = min(b1, m1)
    else:
        m1 -= bet
        if m1 == 0:
            print("BROKE")
            break
        bet = min(2*bet, m1)
    rd += 1
if m1 > 0:
    print(m1)
