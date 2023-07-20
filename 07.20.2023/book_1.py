# from book import number_of_book, decrease_book
import book

def rental_book(name,num_book):
    book.decrease_book(num_book)
    print('남은 책의 수:', book.number_of_book)
    print(f'{name}님이 {num_book}권의 책을 대여하였습니다.')
    
rental_book('홍길동',3)