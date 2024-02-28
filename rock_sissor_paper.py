import random
import sys

score_dic = {'승': 0, '패': 0, '무승부': 0}


def make_answer():
    """
    컴퓨터가 가위 바위 보를 냅니다.
    """
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        answer = '가위'
    elif rand_num == 2:
        answer = '바위'
    elif rand_num == 3:
        answer = '보'
    return answer


def check_winner(answer, user_answer):
    """
    사용자의 결과와 컴퓨터의 결과를 비교하여 승/패/무승부를 판단합니다.

    Args:
        answer (str): 가위/바위/보
        user_answer (str): 가위/바위/보

    Returns:
        str: 승/패/무승부
    """
    if user_answer == answer:
        judge = '무승부'
    elif user_answer == '가위':
        if answer == '바위':
            judge = '패'
        elif answer == '보':
            judge = '승'
    elif user_answer == '보':
        if answer == '가위':
            judge = '패'
        elif answer == '바위':
            judge = '승'
    elif user_answer == '바위':
        if answer == '보':
            judge = '패'
        elif answer == '가위':
            judge = '승'
    return judge


def print_save_judge(answer, user_answer, judge):
    """
    결과를 사용자에게 보여주고 저장합니다.

    Args:
        answer (str): 가위/바위/보
        user_answer (str): 가위/바위/보
        judge (str): 승/패/무승부
    """
    print(f'사용자: {user_answer}, 컴퓨터:{answer}')
    print(f'결과: {judge}')
    print()
    score_dic[judge] = score_dic[judge] + 1


if __name__ == '__main__':
    print('::: 가위 바위 보 게임에 오신 것을 환영 합니다. :::')
    print('1. 게임을 시작')
    print('2. 나가기')
    value = int(input('>>> 진행하고 싶은 번호를 입력해주세요:'))
    while value not in [1, 2]:
        print('잘못된 번호를 입력했습니다.\n')
        value = int(input('>>> 진행하고 싶은 번호를 입력해주세요:'))
    if value == 1:
        pass
    elif value == 2:
        print('게임을 종료합니다.')
        sys.exit()

    # 게임 시작
    while True:
        user_answer = input('>>> 가위, 바위, 보 중 하나를 입력해주세요:')
        while user_answer not in ['가위', '바위', '보']:
            print('유효한 입력이 아닙니다.\n')
            user_answer = input('>>> 가위, 바위, 보 중 하나를 입력해주세요:')
        answer = make_answer()
        judge = check_winner(answer, user_answer)
        print_save_judge(answer, user_answer, judge)

        # 게임 재시작 질문
        print('1. 게임 계속 진행')
        print('2. 게임 재시작 (초기화)')
        print('3. 나가기')
        value = int(input('>>> 진행하고 싶은 번호를 입력해주세요:'))
        while value not in [1, 2, 3]:
            print('잘못된 번호를 입력했습니다.\n')
            value = int(input('>>> 진행하고 싶은 번호를 입력해주세요:'))
        if value == 1:
            pass
        elif value == 2:
            print(f'최종 점수 : {score_dic}')
            print('점수를 초기화 합니다')
            score_dic = {'승': 0, '패': 0, '무승부': 0}
            print(f'점수 : {score_dic}')
            print()
        elif value == 3:
            print('게임을 마쳤습니다.')
            print(score_dic)
            break
    sys.exit()
