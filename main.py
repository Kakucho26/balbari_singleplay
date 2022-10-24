from judge import Judge
from player import Player
from computer import Computer
from howtoplay import howtoplay

judge = Judge()
player1 = Player()
player2 = Computer()

def main():

    howtoplay()
    
    player1.show()

    input('''
처음 받은 덱이다. 왈!
''')

    win_or_lose = False
    round_now = 1

    while round_now <= judge.round:
        print(f'''
{round_now} 라운드. 왈!
''')
        player1.draw(player1.mydeck)
        player2.draw(player2.mydeck)

        #print('컴퓨터: ')
        #player2.show()
        #print(' ')

        #print('플레이어: ')
        player1.show()

        player1.throw()
        player2.throw()

        balbari_player = judge.isBalbari(player1.mydeck)
        balbari_computer = judge.isBalbari(player2.mydeck)
        
        if balbari_player:
            judge.winMessage(player2)

            win_or_lose = True
            break
        elif balbari_computer:
            judge.loseMessage(player2)
            win_or_lose = True
            break
        round_now += 1

    if win_or_lose == False:
        judge.loseMessage(player2)


if __name__ == "__main__":
    main()