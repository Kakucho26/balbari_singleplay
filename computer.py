import random
from initial import createDeck, deck_left


'''
플레이어의 대진상대 컴퓨터.

mydeck 랜덤으로 생성

show() 가진 카드 보여주기
draw() 카드 추가해서 5장으로 만들기
throw() 카드 5장 중에서 한장 알고리즘대로 버리기
'''

class Computer:
    def __init__(self):
        self.mydeck = createDeck()

    def show(self):
        for i,j in enumerate(self.mydeck):
            print(f"{i+1}: {j[0]} {j[1]}")

    def draw(self, mydeck):
        mydeck.append(deck_left[0])
        deck_left.remove(deck_left[0])

    def throw(self):
        to_throw = [(i,j) for i,j in self.mydeck if j not in ('A', 'J', 'Q', 'K')]
        throw = random.choice(to_throw)
        self.mydeck.remove(throw)

if __name__ == "__main__":
    player2 = Computer()
    print(player2.coin)
    print(player2.mydeck)