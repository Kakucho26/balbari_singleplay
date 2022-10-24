class Judge:
    def __init__(self):
        self.round = 5
        self.betting = 1000

    def isBalbari(self, mydeck):
        for i,j in mydeck:
            if j not in ('A', 'J', 'Q', 'K'):
                return False
        else:
            return True

    def loseMessage(self, computer):
        print('''
        패배했다.. 왈..
        ''')
        print('컴퓨터의 덱:')
        computer.show()

    def winMessage(self, computer):
        print('''
        승리했다! 왈!
        ''' )
        print('컴퓨터의 덱:')
        computer.show()

        
    def draw(self):
        pass