from judge import Judge


judge = Judge()

def howtoplay():
    welcome = input ('''

반갑다, 왈! 나는 강아지 발바리라고 한다!
발바리라는 카드게임을 들어보았나? Y/N ''')

    while not (welcome == 'Y' or welcome == 'N'):
        welcome = input('예는 Y, 아니오는 N이다! ')

    if welcome == 'N':
        print('''
당연히 들어본 적이 없겠지! 지금 만들었으니까!
발바리는 트럼프카드 중 조커를 뺀 52장으로 하는 게임이다. 왈!
모든 트럼프 카드는 문양과 글자가 있다. 발바리에선 글자가 중요한데
글자는 A, 2~10, J,Q,K가 있다. 알파벳과 숫자가 있지? 왈?''')

        input(f'''
내가 가진 카드 4장이 모두 알파벳 카드면 발바리가 났다고 한다!
카드 한 장을 줍고 버리기를 반복하며 발바리가 날 때까지
승부를 겨루는 것이 바로 발바리!
{judge.round} 라운드가 끝날 때까지 아무도 발바리를 못 내면 컴퓨터의 승,
동시에 발바리가 나면 플레이어의 승이다! 왈!
시ㅡ작!
''')

    elif welcome == 'Y':
        print('''
바로 시작하겠다, 왈!
''')
