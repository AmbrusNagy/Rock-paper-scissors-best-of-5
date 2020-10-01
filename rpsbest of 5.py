import random


player1 = 0
player2 = 0

for i in range(5):
    print('0 = rock, 1 = paper, 2 = scissors')
    p1 = int(input('Player1: '))
    p2 = random.randint(0, 2)
    
    if p1 == 0:
        print('Player1 has chosen Rock!')
    if p1 == 1:
        print('Player1 has chosen paper!')
    if p1 == 2:
        print('Player1 has chosen scissors!') 
    if p2 == 0:
        print('Player2 has chosen Rock!')
    if p2 == 1:
        print('Player2 has chosen paper!')
    if p2 == 2:
        print('Player2 has chosen scissors!')

    if p1 == p2 :
        print('Tie!')
    if p1 == 0 and p2 ==1 or p1 == 1 and p2 == 2 or p1 == 2 and p2 == 0:
        player2 += 1
        print('Player2 + 1')
        print('Player1:', player1,'Player2:', player2)
    if p1 == 1 and p2 ==0 or p1 == 2 and p2 == 1 or p1 == 0 and p2 == 2:
        player1 +=1
        print('Player1 + 1')
        print('Player1:', player1,'Player2:', player2)
    if p1 > 2:
        print('ERROR!')
    if p2 > 2:
        print('ERROR!')

if player1 < player2:
    print('Winner: Player2')
else:
    print('Winner: Player1')