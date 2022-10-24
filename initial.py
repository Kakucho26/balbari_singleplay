import random

suit = ['♠', '◆', '♥', '♣']
num = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

card = []
for i in suit:
    for j in num:
        card.append((i,j))

card_balbari = [(i,j) for i,j in card if j in ('A', 'J', 'Q', 'K')]
none_balbari = [(i,j) for i,j in card if j not in ('A', 'J', 'Q', 'K')]

#카드 중 발바리가 가능한 카드를 두 장, 불가능한 카드를 두 장 받는다.

def createDeck():
    mydeck = random.sample(card_balbari, 2)
    mydeck.extend(random.sample(none_balbari, 2))
    return mydeck
'''
mydeck = random.sample(card_balbari, 2)
mydeck.extend(random.sample(none_balbari, 2))
'''
mydeck = createDeck()
deck_left = card[:]
for each in mydeck:
    deck_left.remove(each)
random.shuffle(deck_left)

if __name__ == "__main__":
    print(mydeck)
    print(deck_left)