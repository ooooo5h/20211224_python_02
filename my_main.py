# (my_math)모듈 내부의 함수(add)를 따로 불러와서 바로 사용
# import my_math 로 활용하기 번거로웡!!

from my_math import add, mul, div  # 하나의 모듈ㅇ에서 여러개의 함수를 한꺼번에 불러올 수 있다. 

mul(10, 20)
add(10, 20)
div(10,20)