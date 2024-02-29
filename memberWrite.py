"""
**과제 내용:**

1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

**평가**

- 클래스와 인스턴스 개념을 설명할 수 있는가?
- 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
- 클래스를 정의할 수 있는가?
- 인스턴스를 생성할 수 있는가?
"""
# ----- 코드 정의 ------
import hashlib
import secrets


class Member:
    def __init__(self, name, username, password) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.hash = False
        self.salt = None

    def display(self):
        print('회원 이름:', self.name)
        print('회원 아이디:', self.username)
        print()

    def password_hash(self):
        if not self.hash:
            print('암호의 해싱을 실시합니다.')
            self.salt = secrets.token_hex(16)
            salted_password = self.salt + self.password
            self.password = hashlib.sha256(
                salted_password.encode()).hexdigest()
            self.hash = True
            print('암호의 해싱 완료.')
        else:
            print('암호가 이미 해싱 되었습니다.')


class Post:
    def __init__(self, title, content, author) -> None:
        self.title = title
        self.content = content
        self.author = author


members = []
posts = []

# 회원 추가 및 출력 미션
member1 = Member('이윤후', 'beta2020', 'pathWorld!@#')
member2 = Member('이윤재', 'smartstupig', '0325PP$%')
member3 = Member('이윤성', 'lazygoing', 'paint0131!')
member1.password_hash()
member2.password_hash()
member3.password_hash()
members.append(member1)
members.append(member2)
members.append(member3)

print('[ members 회원들 출력 ]')
for member in members:
    member.display()
print()

# 각각의 회원이 게시글을 세개 이상 작성하는 미션
# 1. 9개 이상의 글을 작성하여 posts 리스트에 append로 추가
# 2. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
# 3. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
post1 = Post('제목 테스트1', '내용 테스트1', members[0].name)
post2 = Post('김 오웬의 꿈',
             '''
하늘의 별들이 미소를 지어
밤의 꿈을 채우는 김 오웬
길게 뻗은 언덕 위에서
저녁 태양에 맞이하는 꿈''',
             members[0].name)
post3 = Post('장미꽃의 미소',
             '''
붉은 장미는 사랑의 미소
가시 속에도 숨겨진 설렘
정열의 불꽃 타오르면
장미꽃은 영원한 사랑''',
             members[0].name)
post4 = Post('바다의 노래',
             '''
파도가 부르는 바다의 노래
푸르게 퍼져 휘날리는 감성
모래 위에 쓰여진 시
바다의 속삭임이 되어
''',
             members[0].name)
post5 = Post('가을의 선율',
             '''
단풍이 노래하는 가을의 날
바람은 춤추며 나뭇가지에
종이 비행기처럼 날아가는
가을의 선율이 흐른다
''',
             members[1].name)
post6 = Post('제목 테스트2', '내용 테스트2', members[1].name)
post7 = Post('밤하늘의 별빛',
             '''
어둠에 가려진 밤하늘에
별빛이 빛나는 풍경
우리의 소망은 별과 함께
저 멀리 속삭임으로 날아가
''',
             members[1].name)
post8 = Post('봄의 노래',
             '''
꽃들이 꽃피우는 봄의 노래
작은 새들이 지저귀는 숲
바람에 실려 나뭇잎들이
봄의 노래가 만들어진다
''',
             members[1].name)
post9 = Post('달빛의 이야기',
             '''
달빛이 비치는 어둠의 밤
별들은 이야기를 나눈다
달빛이 비추는 풍경 속에서
우리의 꿈이 펼쳐진다
''',
             members[2].name)
post10 = Post('제목 테스트3', '내용 테스트3', members[2].name)
post11 = Post('사랑의 향기',
              '''
꽃들이 피어나는 봄날에
사랑은 꽃향기처럼 피어난다
매일매일 느끼는 그 향기는
영원한 사랑의 기억이 된다
''',
              members[2].name)
posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)
posts.append(post5)
posts.append(post6)
posts.append(post7)
posts.append(post8)
posts.append(post9)
posts.append(post10)
posts.append(post11)

print('[ 특정 유저의 게시글 출력 ]')
for post in posts:
    if post.author == members[0].name:
        print('작가:', post.author)
        print('제목:', post.title)
        print('내용:', post.content)
        print()
print()

print('[ "테스트"가 content에 포함된 게시글 출력 ]')
for post in posts:
    if post.content.find('테스트') != -1:
        print('작가:', post.author)
        print('제목:', post.title)
        print('내용:', post.content)
        print()


if __name__ == '__main__':
    """
    ** 추가 과제 **
    1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
    2. post도 터미널에서 생성할 수 있게 해주세요.
    3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
    """
    while True:
        print('1. 맴버 추가')
        print('2. 글 추가')
        menu_answer = input('>>> 메뉴를 선택해주세요: (1 혹은 2)')
        try:
            if int(menu_answer) in [1, 2]:
                menu_answer = int(menu_answer)
                break
        except ValueError:
            print('올바른 메뉴를 입력해주세요. 메뉴는 1과 2만 선택 가능합니다.')
    if menu_answer == 1:
        name = input('>>> 이름을 입력해주세요: ')
        user_name = input('>>> 아이디를 입력해주세요: ')
        while True:
            password = input('>>> 비밀번호를 입력해주세요: ')
            re_password = input('>>> 비밀번호를 다시 한번 입력해주세요: ')
            if password == re_password:
                break
            else:
                print('입력한 비밀번호가 다릅니다. 비밀번호를 다시 입력해주세요.')
        print()
        member = Member(name, user_name, password)
        member.password_hash()
        members.append(member)
        print(f'{member.name}({member.username}) 추가가 성공적으로 완료되었습니다.')
    elif menu_answer == 2:
        while True:
            # TODO author가 Member에 있는지 validation
            author = input('>>> 작가를 입력해주세요:')
            title = input('>>> 제목를 입력해주세요:')
            content = input('>>> 내용를 입력해주세요:')
            print()
            print('>>> 작성한 내용이 맞는지 확인해주세요.')
            print()
            print('작가:', author)
            print('제목:', title)
            print('내용:', content)
            print()
            print('작성한 내용이 맞는지 확인해주세요')
            print('1. 확인')
            print('2. 재작성')
            # TODO 입력 값 validation
            valid_answer = int(input('>>> 답변:'))
            if valid_answer == 1:
                post = Post(author, title, content)
                posts.append(post)
                print('글 작성이 완료되었습니다!')
                break
