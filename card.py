# 개념 설명용 클래스
# 포커 카드를 표현하는 클래스

class Card:

    # 카드의 가로길이 / 세로길이 => 각각이 별개로 갖는 게 아니라, 모든 카드가 공유해야하는 값(같은 값 유지)
    # 여기에 만든 변수들은, '클래스 변수'로 동작 => 모든 객체가 동일한 값을 갖는다.
    width = 5
    height = 7
    
    
    def __init__(self, pattern, number):
        # 객체 변수 => 각 카드 한장 한장이 갖는 모양 / 숫자
        self.pattern = pattern
        self.number = number
        