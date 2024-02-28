"""
    **내용:**

1. 플레이어와 컴퓨터가 참여하는 업다운 게임을 만드세요.
1. 프로그램은 다음과 같은 기능을 포함해야 합니다.
    - 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다.
    - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다.
    - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다.
    - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.

**추가 도전 과제:**

1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.
2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.

**평가**

- input을 이용해서 사용자의 입력을 받을 수 있는가?
- input으로 받은 값을 string에서 int로 바꿀 수 있는가?
- while문을 사용하고 특정조건에서 break를 걸어서 멈출 수 있는가?
- if문을 이용해서 조건에 따른 코드 실행을 바꿀 수 있는가?

"""

import random


class Updown:
    def __init__(self) -> None:
        self.record = {'시도 횟수': 0}
        self.rand_num = random.randint(1, 100)

    def reset_game(self):
        print('새로운 숫자를 맞춰보세요!')
        self.record = {'시도 횟수': 0}
        self.rand_num = random.randint(1, 100)

    def start_game(self):
        print('UpDown 게임에 오신 것을 환영합니다')
        print('1. 게임 시작하기')
        print('2. 게임 종료하기')
        menu_num = input('>>> 메뉴 번호를 선택해주세요 :')
        while True:
            answer = self.validate_start_game(menu_num)
            if answer:
                break
            else:
                print('1. 게임 시작하기')
                print('2. 게임 종료하기')
                menu_num = input('>>> 메뉴 번호를 선택해주세요 :')
        return int(menu_num)

    def validate_start_game(self, menu_num):
        try:
            if int(menu_num) not in [1, 2]:
                print('WARNING : 1,2 중 하나만 입력하세요')
                return False
            else:
                return True
        except ValueError:
            print('WARNING : 숫자를 입력하셔야 합니다')
            return False

    def validate_input_num(self, input_num):
        try:
            if int(input_num) > 100:
                print('WARNING : 100 이하의 숫자만 입력하셔야 합니다.')
                return False
            elif int(input_num) < 1:
                print('WARNING : 1 이상의 숫자만 입력하셔야 합니다.')
                return False
            else:
                return True
        except ValueError:
            print('WARNING : 숫자를 입력하셔야 합니다')
            return False

    def check_input_num(self, input_num):
        if int(input_num) == self.rand_num:
            print('정답을 맞히셨습니다')
            return True
        elif int(input_num) > self.rand_num:
            print('Down')
            return False
        elif int(input_num) < self.rand_num:
            print('Up')
            return False


if __name__ == '__main__':
    game = Updown()
    menu = game.start_game()
    if menu == 1:
        while True:
            input_num = input('>>> 숫자를 입력하세요 : ')
            validate_answer = game.validate_input_num(input_num)
            if validate_answer:
                game.record['시도 횟수'] = game.record['시도 횟수'] + 1
                check_answer = game.check_input_num(input_num)
                if check_answer:
                    print('시도한 횟수:', game.record['시도 횟수'])
                    restart_answer = input('>>> 다시 시작하시겠습니까? (y/n):')
                    if restart_answer.upper() == 'Y':
                        game.reset_game()
                    else:
                        print('게임을 종료합니다.')
                        break
    else:
        print('게임을 종료합니다.')
