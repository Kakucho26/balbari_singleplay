from initial import createDeck, deck_left


'''
실제로 플레이하는 사람.

coin 3000개로 시작
mydeck 랜덤으로 생성

show() 가진 카드 보여주기
draw() 카드 추가해서 5장으로 만들기
throw() 카드 5장 한 장 선택해서 버리기
'''

class Player:
    def __init__(self):
        self.coin = 3000
        self.mydeck = createDeck()

    def show(self):
        for i,j in enumerate(self.mydeck):
            print(f"{i+1}: {j[0]} {j[1]}")

    def draw(self, mydeck):
        mydeck.append(deck_left[0])
        deck_left.remove(deck_left[0])

    def throw(self):
        number = input("버릴 카드 한 장을 선택해라, 왈! 1~5: ")
        while number not in ('1','2','3','4','5'):
            number = input("버릴 카드 한 장을 선택해라, 왈!. 1~5: ")
        number = int(number)
        self.mydeck.remove(self.mydeck[number-1])



if __name__ == "__main__":
    player1 = Player()
    print(player1.mydeck)