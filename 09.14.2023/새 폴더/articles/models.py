from django.db import models

# Create your models here.
# 테이블에 대응하는 클래스를 정의
class Article(models.Model): # 상속  # 테이블이름: 앱 이름_클래스 이름
    # 반드시 장고에 의해 생성되는 필드:  id (pk= primary key)
    # 테이블의 필드에 대응하는 클래스 변수 선언
    title = models.CharField(max_length=10)  # model 모듈의 CharField클래스의 인스턴스(Article의 변수)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20,default='unknown')


    def __str__(self): # 이게 무슨 역할?
        return self.title
