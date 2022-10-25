# **발바리**

카드게임의 룰을 창작해보았다. 

* 트럼프카드 중 조커 두 장을 뺀 52장으로 한다.

* **승리 조건**: 카드 네 장이 모두 A, J, Q, K로만 이루어지는 것 (발바리)

* **규칙**: 처음 카드 네 장을 받는다. 두 장은 알파벳 카드, 두 장은 숫자 카드이다.

* 플레이어와 대전 상대가 카드 한 장을 줍고 버리기를 반복하며 발바리를 완성한다.

* 정해진 라운드가 (기본 5) 끝날 때까지 아무도 발바리를 못 내면 대전 상대의 승,

* 동시에 발바리가 나면 플레이어의 승.

**파일 설명**

* **initial.py** 카드를 섞고 처음 받는 카드를 생성하는 과정
* **player.py** 플레이어 클래스
* **computer.py** 대전 상대 클래스
* **judge.py** 라운드, 발바리 판명, 승패 메시지를 담은 심판 클래스
* **howtoplay.py** 게임 규칙 설명 메시지
* **main.py** 실행 파일
