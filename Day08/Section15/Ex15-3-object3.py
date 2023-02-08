class Book:
    def sef_info(self, title, author):
        self.title = title # 나중에 들어오게 될 변수를 나 자신에게 정의해 줌
        self.author = author # 나중에 들어오게 될 변수를 나 자신에게 정의해 줌

    def print_info(self):
        print('책 제목 : {}'.format(self.title))
        print('책 저자 : {}'.format(self.author))

# book1, book2 인스턴트 생성
book1 = Book()
book2 = Book()

# book1 객체에서 class 메소드 활용하기

book1.sef_info("나무","베르나르 베르베르")
book1.print_info()

#book2 객체에서 class 메소드 활용하기

book2.sef_info("빨간망토","안데르센")
book2.print_info()

book_list = [book1, book2]

for book in book_list:
    book.print_info()