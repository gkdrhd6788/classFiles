list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','난중일기','백호집','홍길동전','만복자서포기']
# all_book = True  # Flag변수 활용
for book in rental_book:
    if book not in list_of_book:
        all_book = False
        print(f'{book}은/는 보유하고 있지 않습니다.')
        break

# if all_book:     
#      print('모든 도서가 대여 가능한 상태입니다')
else:    #for else문 사용가능
    print('모든 도서가 대여 가능한 상태입니다')



##for 문을 두번 돌려서 해보자(강사님 답안 참조)