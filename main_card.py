from card import Card

# 두장의 카드 생성
card1 = Card('스페이드', 2)
card2 = Card('하트', 7)

# card의 가로길이(Card 클래스 자체의 속성)만 4로 변경
Card.width = 4
# Card의 가로/세로길이는 클래스 변수라서 Card.변수로 접근이 가능하다.
# 하지만, 각 카드 객체의 무늬/숫자는 각 객체에 연결된 변수라서 Card.변수로는 접근이 불가능
# print(Card.pattern)    >> 이런 행위는 불가능!! 

# 두 장의 카드 각각의 가로길이를 출력해보자
print(f'스페이드2의 가로길이? : {card1.width}')
print(f'하트7의 가로 길이 : {card2.width}')
# 위처럼 잘 안쓰고

# 아래처럼 쓴다. 클래스 자체의 변수
print(f'카드 전체의 가로길이 : {Card.width}')


# 카드 클래스 자체의 기능 (클래스 설명 기능 실행)
Card.print_card_class_info()