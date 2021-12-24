class Book:
    def __init__(self, title, rent_fee, limit_age):
        self.title = title
        self.rent_fee = rent_fee
        self.limit_age = limit_age
        
        self.rent_user = None
        
    def print_book_info(self):
        
        print('===== 도서 정보 출력 ======')
        print(f'제목 : {self.title}')
        print(f'대여료 : {self.rent_fee}P')
        print(f'연령 제한 : {self.limit_age}세 이용가')            
        
        if self.rent_user:
            pass
        else:
            print('대여해간 사람이 없습니다.')
            
            
    def rent_book_to_user(self, user):
        
        
        # 검사해야하는 각 항목들의 검사 결과를 변수에 담아두자 
        is_point_ok = (user.point >= self.rent_fee)
        
        is_age_ok = (user.get_age(2021) >= self.limit_age)

        is_rent_available = (self.rent_user == None)
                

        # 모든 검사를 통과해야 True가 리턴        
        return is_point_ok and is_age_ok and is_rent_available
